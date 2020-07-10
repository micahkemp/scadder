{% block includes %}{% endblock -%}
module {{ component.module_name }}() {
    {% block call_module %}{% endblock %}
}

// call module when run directly
{{ component.module_name }}();
