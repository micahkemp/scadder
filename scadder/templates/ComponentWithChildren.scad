{% extends "ComponentBase.scad" %}
{% block includes -%}
// use modules
{% for child in component.children -%}
use <{{ child.module_name }}/{{ child.filename() }}>
{% endfor %}
{% endblock %}
{% block call_module -%}
    {{ component.formatted_call_module() }} {
        {%- for child in component.children %}
        {{ child.module_name }}();
        {%- endfor %}
    }
{%- endblock %}
