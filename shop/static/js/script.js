const main = () => {
    $('#id_publish_date').datetimepicker({
        format: 'YYYY-MM-DD HH:mm'
    });
};

$(document).ready(main);
