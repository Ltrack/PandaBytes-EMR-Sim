
function setPatient(mrn) {
    console.log('Setting patient:', mrn);
    $.ajax({
        url: '/set_patient/' + mrn,
        type: 'GET',
        success: function () {
            // Redirect to the patient list page after setting the patient.
            window.location.href = '/summary'; // You can change this URL as needed.
        },
        error: function (error) {
            console.error('Error setting patient:', error);
        }
    });
}
