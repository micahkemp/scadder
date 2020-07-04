{% extends "SolidObjectBase.scad" %}
{% block call_module -%}
    {{ solid_object.formatted_call_module() }};
{%- endblock %}
