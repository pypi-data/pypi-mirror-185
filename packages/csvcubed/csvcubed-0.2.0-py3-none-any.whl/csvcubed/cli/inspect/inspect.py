"""
Inspect Command
---------------

Output CSV-W metadata in a user-friendly format to the CLI for validation.
"""

import logging
from os import linesep
from pathlib import Path
from typing import Tuple

import rdflib

from csvcubed.cli.inspect.metadatainputvalidator import MetadataValidator
from csvcubed.cli.inspect.metadataprinter import MetadataPrinter
from csvcubed.models.csvcubedexception import FailedToLoadRDFGraphException
from csvcubed.models.csvwtype import CSVWType
from csvcubed.utils.sparql_handler.code_list_state import CodeListState
from csvcubed.utils.sparql_handler.data_cube_state import DataCubeState
from csvcubed.utils.tableschema import CsvwRdfManager

_logger = logging.getLogger(__name__)


def inspect(csvw_metadata_json_path: Path) -> None:
    """
    Command for validating CSV-W metadata files through the CLI.

    Member of :file:`./inspect.py`

    :return: `None`
    """
    _logger.debug(f"Metadata json-ld path: {csvw_metadata_json_path.absolute()}")

    csvw_rdf_manager = CsvwRdfManager(csvw_metadata_json_path)
    csvw_metadata_rdf_graph = csvw_rdf_manager.rdf_graph

    if csvw_metadata_rdf_graph is None:
        raise FailedToLoadRDFGraphException(csvw_metadata_json_path)

    csvw_metadata_rdf_validator = MetadataValidator(
        csvw_metadata_rdf_graph, csvw_metadata_json_path
    )
    csvw_type = csvw_metadata_rdf_validator.detect_csvw_type()

    (
        type_printable,
        catalog_metadata_printable,
        dsd_info_printable,
        codelist_info_printable,
        dataset_observations_printable,
        val_counts_by_measure_unit_printable,
        codelist_hierarchy_info_printable,
    ) = _generate_printables(
        csvw_type, csvw_metadata_rdf_graph, csvw_metadata_json_path
    )

    print(f"{linesep}{type_printable}")
    print(f"{linesep}{catalog_metadata_printable}")
    if csvw_type == CSVWType.QbDataSet:
        print(f"{linesep}{dsd_info_printable}")
        print(f"{linesep}{codelist_info_printable}")
    print(f"{linesep}{dataset_observations_printable}")
    if csvw_type == CSVWType.QbDataSet:
        print(f"{linesep}{val_counts_by_measure_unit_printable}")
    if csvw_type == CSVWType.CodeList:
        print(f"{linesep}{codelist_hierarchy_info_printable}")


def _generate_printables(
    csvw_type: CSVWType,
    csvw_metadata_rdf_graph: rdflib.ConjunctiveGraph,
    csvw_metadata_json_path: Path,
) -> Tuple[str, str, str, str, str, str, str]:
    """
    Generates printables of type, metadata, dsd, code list, head/tail and value count information.

    Member of :file:`./inspect.py`

    :return: `Tuple[str, str, str, str, str]` - printables of metadata information.
    """
    metadata_printer: MetadataPrinter

    if csvw_type == CSVWType.QbDataSet:
        data_cube_state = DataCubeState(
            csvw_metadata_rdf_graph, csvw_metadata_json_path
        )
        metadata_printer = MetadataPrinter(
            data_cube_state=data_cube_state,
            code_list_state=None,
            csvw_type=csvw_type,
            csvw_metadata_rdf_graph=csvw_metadata_rdf_graph,
            csvw_metadata_json_path=csvw_metadata_json_path,
        )
    else:
        code_list_state = CodeListState(csvw_metadata_rdf_graph)
        metadata_printer = MetadataPrinter(
            data_cube_state=None,
            code_list_state=code_list_state,
            csvw_type=csvw_type,
            csvw_metadata_rdf_graph=csvw_metadata_rdf_graph,
            csvw_metadata_json_path=csvw_metadata_json_path,
        )

    type_info_printable: str = metadata_printer.type_info_printable
    catalog_metadata_printable: str = metadata_printer.catalog_metadata_printable
    dsd_info_printable: str = (
        metadata_printer.dsd_info_printable if csvw_type == CSVWType.QbDataSet else ""
    )
    codelist_info_printable: str = (
        metadata_printer.codelist_info_printable
        if csvw_type == CSVWType.QbDataSet
        else ""
    )
    dataset_observations_info_printable: str = (
        metadata_printer.dataset_observations_info_printable
    )
    dataset_val_counts_by_measure_unit: str = (
        metadata_printer.dataset_val_counts_by_measure_unit_info_printable
        if csvw_type == CSVWType.QbDataSet
        else ""
    )
    codelist_hierarchy_info_printable: str = (
        metadata_printer.codelist_hierachy_info_printable
        if csvw_type == CSVWType.CodeList
        else ""
    )

    return (
        type_info_printable,
        catalog_metadata_printable,
        dsd_info_printable,
        codelist_info_printable,
        dataset_observations_info_printable,
        dataset_val_counts_by_measure_unit,
        codelist_hierarchy_info_printable,
    )
