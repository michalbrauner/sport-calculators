$(document).ready(function () {

    var calculatorRunningForm = $('#calculator-running form');

    $(calculatorRunningForm).on('submit', function (e) {
        e.preventDefault();

        $.post($(this).attr('action'), $(this).serialize(), function (response) {
            console.log(response);
        });

        return false;

    });

    var calculator = new CalculatorRunning(calculatorRunningForm);
    calculator.setFieldsState();

    $(calculatorRunningForm).find('input').on('keyup', function (e) {
        calculator.setFieldsState();
    });
});

function CalculatorRunning(form) {
    this.form = form;
    this.distanceSelector = 'input[name=distance]';
    this.tempoMinutesSelector = 'input[name=tempo_minutes]';
    this.tempoSecondsSelector = 'input[name=tempo_seconds]';
    this.timeHoursSelector = 'input[name=time_hours]';
    this.timeMinutesSelector = 'input[name=time_minutes]';
    this.timeSecondsSelector = 'input[name=time_seconds]';

    this.setFieldsState = function () {

        var hasDistance = $.trim(this.getField(this.distanceSelector).val()) != '';
        var hasTempo = this.hasTempo();
        var hasTime = this.hasTime();

        this.setDisableAttributeToEditForTime(hasDistance && hasTempo);
        this.setDisableAttributeToEditForTempo(hasDistance && hasTime);
        this.setDisableAttributeToEditForField(this.distanceSelector, hasTempo && hasTime);
    };

    this.getField = function (selector) {
        return $(this.form).find(selector);
    };

    this.hasTime = function () {
        var hasTimeHours = $.trim(this.getField(this.timeHoursSelector).val()) != '';
        var hasTimeMinutes = $.trim(this.getField(this.timeMinutesSelector).val()) != '';
        var hasTimeSeconds = $.trim(this.getField(this.timeSecondsSelector).val()) != '';

        return hasTimeHours || hasTimeMinutes || hasTimeSeconds;
    }

    this.hasTempo = function () {
        var hasTempoMinutes = $.trim(this.getField(this.tempoMinutesSelector).val()) != '';
        var hasTempoSeconds = $.trim(this.getField(this.tempoSecondsSelector).val()) != '';

        return hasTempoMinutes || hasTempoSeconds;
    }

    this.setDisableAttributeToEditForTime = function(isDisabled) {
        this.setDisableAttributeToEditForField(this.timeHoursSelector, isDisabled);
        this.setDisableAttributeToEditForField(this.timeMinutesSelector, isDisabled);
        this.setDisableAttributeToEditForField(this.timeSecondsSelector, isDisabled);
    }

    this.setDisableAttributeToEditForTempo= function(isDisabled) {
        this.setDisableAttributeToEditForField(this.tempoMinutesSelector, isDisabled);
        this.setDisableAttributeToEditForField(this.tempoSecondsSelector, isDisabled);
    }

    this.setDisableAttributeToEditForField = function(selector, isDisabled) {
        this.getField(selector).prop('disabled', isDisabled);
    }
}
