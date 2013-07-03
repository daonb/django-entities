from rest_framework import serializers
from entities import models
from entities.utils import translated_fields


class EntityBase(serializers.HyperlinkedModelSerializer):
    """The default serialized representation of entities."""

    class Meta:
        model = models.Entity
        fields = ['id', 'url', 'name', 'description', 'code', 'parent',
                  'division', 'sheets', 'created_on', 'last_modified']\
                 + translated_fields(model)


class DivisionBase(serializers.HyperlinkedModelSerializer):
    """The default serialized representation of divisions."""

    class Meta:
        model = models.Division
        fields = ['id', 'url', 'name', 'index', 'budgeting', 'domain',
                  'created_on', 'last_modified'] + translated_fields(model)


class DomainBase(serializers.HyperlinkedModelSerializer):
    """The default serialized representation of domains."""

    class Meta:
        model = models.Domain
        fields = ['id', 'url', 'name', 'measurement_system',
                  'ground_surface_unit', 'currency', 'created_on',
                  'last_modified', 'divisions'] + translated_fields(model)


class DomainDetail(DomainBase):
    """A detailed, related representation of domain."""

    divisions = DivisionBase()


class DivisionDetail(DivisionBase):
    """Used to represent a full relational map of a division."""

    domain = DomainBase()
    # don't show self again on nested objects
    del domain.fields['divisions']

    class Meta(DivisionBase.Meta):
        fields = DivisionBase.Meta.fields + ['entities']

#TODO: change back to HyperlinkedModelSerializer once we fix the url of DenormalizedSheetItem
class SheetBase(serializers.ModelSerializer):
    """The default serialized representation of sheets."""

    period = serializers.Field(source='period')

    class Meta:
        model = models.Sheet
        #TODO: put 'url' back here once we fix the url of DenormalizedSheetItem
        fields = ['id', 'template', 'entity', 'description', 'period',
                  'created_on', 'last_modified'] + translated_fields(model)


class EntityDetail(EntityBase):
    """A detailed, related representation of entities."""

    sheets = SheetBase()
