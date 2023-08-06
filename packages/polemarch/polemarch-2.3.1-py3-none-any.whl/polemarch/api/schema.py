from drf_yasg.inspectors.base import FieldInspector, NotHandled
from drf_yasg import openapi
from vstutils.api.schema.schema import VSTAutoSchema
from vstutils.api.schema.inspectors import field_extra_handler

from .v2.serializers import InventoryAutoCompletionField


class InventoryFieldInspector(FieldInspector):
    def field_to_swagger_object(self, field, swagger_object_type, use_references, **kw):
        # pylint: disable=invalid-name
        if not isinstance(field, InventoryAutoCompletionField):
            return NotHandled

        SwaggerType, _ = self._get_partial_types(
            field, swagger_object_type, use_references, **kw
        )
        kwargs = {
            'type': openapi.TYPE_INTEGER if field.real_type == int else openapi.TYPE_STRING,
            'format': 'inventory'
        }

        return SwaggerType(**field_extra_handler(field, **kwargs))


class PolemarchAutoSchema(VSTAutoSchema):
    field_inspectors = [
        InventoryFieldInspector,
    ] + VSTAutoSchema.field_inspectors
