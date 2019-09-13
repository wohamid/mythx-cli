import abc
from typing import List, Union

from mythx_models.response import (
    AnalysisInputResponse,
    AnalysisListResponse,
    AnalysisStatusResponse,
    DetectedIssuesResponse,
    VersionResponse,
)


class BaseFormatter(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def format_analysis_list(
        obj: Union[AnalysisListResponse, List[AnalysisStatusResponse]]
    ):
        pass  # pragma: no cover

    @staticmethod
    def format_analysis_status(resp: AnalysisStatusResponse) -> str:
        pass  # pragma: no cover

    @staticmethod
    @abc.abstractmethod
    def format_detected_issues(obj: DetectedIssuesResponse, inp: AnalysisInputResponse):
        pass  # pragma: no cover

    @staticmethod
    @abc.abstractmethod
    def format_version(obj: VersionResponse):
        pass  # pragma: no cover