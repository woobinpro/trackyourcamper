$(document).ready(function(){
    $('.timefilter').pickatime({
        interval: 10
    });
    $('.datefilter').pickadate({
        format: 'mm/dd/yyyy',
        hiddenPrefix: 'prefix__',
        hiddenSuffix: '__suffix'
    });
});