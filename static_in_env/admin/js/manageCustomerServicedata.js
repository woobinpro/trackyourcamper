$(document).ready(function(){
    $('.summernote').each(function(){
        console.log($(this).html());
    });
    $('.summernote').summernote({toolbar: [
        ['style', ['style']],
        ['font', ['bold', 'italic','underline', 'clear']],
        ['fontname', ['fontname']],
        ['color', ['color']],
        ['para', ['ul', 'ol', 'paragraph']],
        ['view', ['fullscreen', 'codeview', 'help']],
      ],});
});