# BSD 3-Clause License; see https://github.com/scikit-hep/awkward-1.0/blob/main/LICENSE

import builtins
import numbers
from datetime import datetime, timedelta

from awkward_cpp.lib import _ext

import awkward as ak

np = ak._nplikes.NumpyMetadata.instance()


def type(array, *, behavior=None):
    """
    Args:
        array: Array-like data (anything #ak.to_layout recognizes).
        behavior (None or dict): Custom #ak.behavior for the output type, if
            high-level.

    The high-level type of an `array` (many types supported, including all
    Awkward Arrays and Records) as #ak.types.Type objects.

    The high-level type ignores layout differences like
    #ak.contents.ListArray versus #ak.contents.ListOffsetArray, but
    not differences like "regular-sized lists" (i.e.
    #ak.contents.RegularArray) versus "variable-sized lists" (i.e.
    #ak.contents.ListArray and similar).

    Types are rendered as [Datashape](https://datashape.readthedocs.io/)
    strings, which makes the same distinctions.

    For example,

        >>> array = ak.Array([[{"x": 1.1, "y": [1]}, {"x": 2.2, "y": [2, 2]}],
        ...                   [],
        ...                   [{"x": 3.3, "y": [3, 3, 3]}]])

    has type

        >>> ak.type(array).show()
        3 * var * {
            x: float64,
            y: var * int64
        }

    but

        >>> array = ak.Array(np.arange(2*3*5).reshape(2, 3, 5))

    has type

        >>> ak.type(array).show()
        2 * 3 * 5 * int64

    Some cases, like heterogeneous data, require [extensions beyond the
    Datashape specification](https://github.com/blaze/datashape/issues/237).
    For example,

        >>> array = ak.Array([1, "two", [3, 3, 3]])

    has type

        >>> ak.type(array).show()
        3 * union[
            int64,
            string,
            var * int64
        ]

    but "union" is not a Datashape type-constructor. (Its syntax is
    similar to existing type-constructors, so it's a plausible addition
    to the language.)
    """
    with ak._errors.OperationErrorContext(
        "ak.type",
        dict(array=array, behavior=behavior),
    ):
        return _impl(array, behavior)


def _impl(array, behavior):
    if isinstance(array, np.dtype):
        return ak.types.ScalarType(
            ak.types.NumpyType(ak.types.numpytype.dtype_to_primitive(array))
        )

    elif isinstance(array, bool):  # np.bool_ in np.generic (above)
        return ak.types.ScalarType(ak.types.NumpyType("bool"))

    elif isinstance(array, numbers.Integral):
        return ak.types.ScalarType(ak.types.NumpyType("int64"))

    elif isinstance(array, numbers.Real):
        return ak.types.ScalarType(ak.types.NumpyType("float64"))

    elif isinstance(array, numbers.Complex):
        return ak.types.ScalarType(ak.types.NumpyType("complex128"))

    elif isinstance(array, datetime):  # np.datetime64 in np.generic (above)
        return ak.types.ScalarType(ak.types.NumpyType("datetime64"))

    elif isinstance(array, timedelta):  # np.timedelta64 in np.generic (above)
        return ak.types.ScalarType(ak.types.NumpyType("timedelta"))

    elif (
        isinstance(array, np.generic)
        or isinstance(array, builtins.type)
        and issubclass(array, np.generic)
    ):
        primitive = ak.types.numpytype.dtype_to_primitive(np.dtype(array))
        return ak.types.ScalarType(ak.types.NumpyType(primitive))

    elif isinstance(array, _ext.ArrayBuilder):
        form = ak.forms.from_json(array.form())
        return ak.types.ArrayType(form.type_from_behavior(behavior), len(array))

    elif isinstance(array, ak.ArrayBuilder):
        behavior = ak._util.behavior_of(array, behavior=behavior)
        form = ak.forms.from_json(array._layout.form())
        return ak.types.ArrayType(form.type_from_behavior(behavior), len(array._layout))

    else:
        behavior = ak._util.behavior_of(array, behavior=behavior)
        layout = ak.to_layout(array, allow_other=True, allow_record=True)
        if layout is None:
            return ak.types.ScalarType(ak.types.UnknownType())

        elif isinstance(layout, ak.record.Record):
            return ak.types.ScalarType(layout.array.form.type_from_behavior(behavior))

        elif isinstance(layout, ak.contents.Content):
            return ak.types.ArrayType(
                layout.form.type_from_behavior(behavior), layout.length
            )

        else:
            raise ak._errors.wrap_error(
                TypeError(f"unrecognized array type: {array!r}")
            )
