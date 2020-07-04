module {{ solid_object.module_name }}() {
    {% block call_module %}{% endblock %}
}

// call module when run directly
{{ solid_object.module_name }}();
