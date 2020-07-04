{% extends "SolidObjectBase.scad" %}
{% block call_module -%}
    {{ solid_object.formatted_call_module() }} {
        {%- for child in solid_object.children %}
        {{ child.module_name }}();
        {%- endfor %}
    }
{%- endblock %}
