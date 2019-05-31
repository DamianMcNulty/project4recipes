// Copyright (c) 2013 Bootsnipp.com
// Copyright (c) 2016 TavoQiqe https://www.facebook.com/tavo.qiqe.lucero

// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

$(document).ready(function () {

  $('.star').on('click', function () {
    $(this).toggleClass('star-checked');
  });

  $('.ckbox label').on('click', function () {
    $(this).parents('tr').toggleClass('selected');
  });

  $('.btn-filter').on('click', function () {
    var $target = $(this).data('target');
    if ($target !== 'all') {
      $('.panel-body').css('display', 'none');
      $('.panel-body[data-status="' + $target + '"]').fadeIn('slow');
    } else {
      $('.panel-body').css('display', 'none').fadeIn('slow');
    }
  });

  var header = document.getElementById("pagination");
  var btns = header.getElementsByClassName("item");
  for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function () {
      var current = document.getElementsByClassName("active");
      current[0].className = current[0].className.replace(" active", "");
      this.className += " active";
    });
  }

});