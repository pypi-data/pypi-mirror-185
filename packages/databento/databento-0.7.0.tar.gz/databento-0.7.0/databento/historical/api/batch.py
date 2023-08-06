from datetime import date
from typing import Any, Dict, List, Optional, Tuple, Union

import pandas as pd
from databento.common.enums import (
    Compression,
    Dataset,
    Delivery,
    Encoding,
    Packaging,
    Schema,
    SplitDuration,
    SType,
)
from databento.common.parsing import (
    maybe_datetime_to_string,
    maybe_values_list_to_string,
)
from databento.common.validation import validate_enum
from databento.historical.api import API_VERSION
from databento.historical.http import BentoHttpAPI


class BatchHttpAPI(BentoHttpAPI):
    """
    Provides request methods for the batch HTTP API endpoints.
    """

    def __init__(self, key: str, gateway: str) -> None:
        super().__init__(key=key, gateway=gateway)
        self._base_url = gateway + f"/v{API_VERSION}/batch"

    def submit_job(
        self,
        dataset: Union[Dataset, str],
        start: Union[pd.Timestamp, date, str, int],
        end: Union[pd.Timestamp, date, str, int],
        symbols: Optional[Union[List[str], str]],
        schema: Union[Schema, str],
        encoding: Union[Encoding, str] = "dbz",
        compression: Optional[Union[Compression, str]] = None,
        split_duration: Union[SplitDuration, str] = "day",
        split_size: Optional[int] = None,
        packaging: Union[Packaging, str] = "none",
        delivery: Union[Delivery, str] = "download",
        stype_in: Union[SType, str] = "native",
        stype_out: Union[SType, str] = "product_id",
        limit: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Request a new time series data batch download from Databento.

        Makes a `POST /batch.submit_job` HTTP request.

        Parameters
        ----------
        dataset : Dataset or str
            The dataset code (string identifier) for the request.
        start : pd.Timestamp or date or str or int
            The start datetime of the request time range (inclusive).
            Assumes UTC as timezone unless passed a tz-aware object.
            If an integer is passed, then this represents nanoseconds since UNIX epoch.
        end : pd.Timestamp or date or str or int
            The end datetime of the request time range (exclusive).
            Assumes UTC as timezone unless passed a tz-aware object.
            If an integer is passed, then this represents nanoseconds since UNIX epoch.
        symbols : List[Union[str, int]] or str
            The product symbols to filter for. Takes up to 2,000 symbols per request.
            If more than 1 symbol is specified, the data is merged and sorted by time.
            If `*` or ``None`` then will be for **all** symbols.
        schema : Schema or str {'mbo', 'mbp-1', 'mbp-10', 'trades', 'tbbo', 'ohlcv-1s', 'ohlcv-1m', 'ohlcv-1h', 'ohlcv-1d', 'definition', 'statistics', 'status'}, default 'trades'  # noqa
            The data record schema for the request.
        encoding : Encoding or str {'dbz', 'csv', 'json'}, default 'dbz'
            The data encoding.
        compression : Compression or str {'none', 'zstd'}, optional
            The data compression format (if any).
            If encoding is 'dbz' then specifying a `compression` is invalid (already zstd compressed).
        split_duration : SplitDuration or str {'day', 'week', 'month', 'none'}, default 'day'
            The maximum time duration before batched data is split into multiple files.
            A week starts on Sunday UTC.
        split_size : int, optional
            The maximum size (bytes) of each batched data file before being split.
        packaging : Packaging or str {'none', 'zip', 'tar'}, default 'none'
            The archive type to package all batched data files in.
        delivery : Delivery or str {'download', 's3', 'disk'}, default 'download'
            The delivery mechanism for the processed batched data files.
        stype_in : SType or str, default 'native'
            The input symbology type to resolve from.
        stype_out : SType or str, default 'product_id'
            The output symbology type to resolve to.
        limit : int, optional
            The maximum number of records for the request. If ``None`` then no limit.

        Returns
        -------
        Dict[str, Any]
            The job info for batch download request.

        Warnings
        --------
        Calling this method will incur a cost.

        """
        if compression is None:
            compression = Compression.NONE

        validate_enum(schema, Schema, "schema")
        validate_enum(encoding, Encoding, "encoding")
        validate_enum(compression, Compression, "compression")
        validate_enum(split_duration, SplitDuration, "duration")
        validate_enum(packaging, Packaging, "packaging")
        validate_enum(delivery, Delivery, "delivery")
        validate_enum(stype_in, SType, "stype_in")
        validate_enum(stype_out, SType, "stype_out")

        params: List[Tuple[str, Optional[str]]] = BentoHttpAPI._timeseries_params(
            dataset=dataset,
            start=start,
            end=end,
            symbols=symbols,
            schema=Schema(schema),
            limit=limit,
            stype_in=SType(stype_in),
            stype_out=SType(stype_out),
        )

        params.append(("encoding", Encoding(encoding).value))
        if (
            Encoding(encoding) != Encoding.DBZ
            or Compression(compression) != Compression.NONE
        ):
            params.append(("compression", Compression(compression).value))
        params.append(("split_duration", SplitDuration(split_duration).value))
        if split_size is not None:
            params.append(("split_size", str(split_size)))
        params.append(("packaging", Packaging(packaging).value))
        params.append(("delivery", Delivery(delivery).value))

        return self._post(
            url=self._base_url + ".submit_job",
            params=params,
            basic_auth=True,
        ).json()

    def list_jobs(
        self,
        states: Optional[Union[List[str], str]] = "received,queued,processing,done",
        since: Optional[Union[pd.Timestamp, date, str, int]] = None,
    ) -> List[Dict[str, Any]]:
        """
        Request all batch job details for the user account.

        The job details will be sorted in order of `ts_received`.

        Makes a `GET /batch.list_jobs` HTTP request.

        Parameters
        ----------
        states : List[str] or str, optional {'received', 'queued', 'processing', 'done', 'expired'}  # noqa
            The filter for jobs states as a list of comma separated values.
        since : pd.Timestamp or date or str or int, optional
            The filter for timestamp submitted (will not include jobs prior to this).

        Returns
        -------
        List[Dict[str, Any]]
            The batch job details.

        """
        params: List[Tuple[str, Optional[str]]] = [
            ("states", maybe_values_list_to_string(states)),
            ("since", maybe_datetime_to_string(since)),
        ]

        return self._get(
            url=self._base_url + ".list_jobs",
            params=params,
            basic_auth=True,
        ).json()
