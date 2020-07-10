{% extends "ComponentBase.scad" %}
{% block call_module -%}
    {{ component.formatted_call_module() }};
{%- endblock %}
