{% extends "SolidObjectBase.scad" %}
{% block includes -%}
// use modules
{% for child in solid_object.children -%}
use <{{ child.module_name }}/{{ child.filename() }}>
{% endfor %}
{% endblock %}
{% block call_module -%}
    {{ solid_object.formatted_call_module() }} {
        {%- for child in solid_object.children %}
        {{ child.module_name }}();
        {%- endfor %}
    }
{%- endblock %}
