$(function () {
    var url = new URL(document.location);
    var params = url.searchParams;
    var period = params.get('period');
    if (period) {
        $('#id_period').val(period);
    }
    $('#id_period').on('change', function (e) {
        this.form.submit();
    });
    $('select.dropdown').dropdown();
    $('#mandarhan').DataTable({
        scrollY: true,
        scrollX: true,
        scrollCollapse: true,
        paging: false,
        // fixedColumns: {
        //     leftColumns: 2
        // },
        ordering: false,
        searching: false,
        info: false,
        order: [[0, 'asc'], [1, 'asc']],
        rowGroup: {
            dataSrc: 1
        },
        columnDefs: [{
            targets: [1],
            visible: false
        }]
    });
});
