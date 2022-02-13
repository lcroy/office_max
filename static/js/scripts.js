function loadImage() {
  ole_profile  = document.getElementById("ole_profile");
  ole_profile.setAttribute('src','static/photos/ole.png');

  simon_profile  = document.getElementById("simon_profile");
  simon_profile.setAttribute('src','static/photos/simon.png');

  dimi_profile  = document.getElementById("dimi_profile");
  dimi_profile.setAttribute('src','static/photos/dimi.png');

  morten_profile  = document.getElementById("morten_profile");
  morten_profile.setAttribute('src','static/photos/morten.png');

  casper_profile  = document.getElementById("casper_profile");
  casper_profile.setAttribute('src','static/photos/casper.png');

  chen_profile  = document.getElementById("chen_profile");
  chen_profile.setAttribute('src','static/photos/chen.png');

}

function ole_b() {
  ole_profile  = document.getElementById("ole_profile");
  ole_profile.setAttribute('src','static/photos/ole_b.png');

  ole_num  = document.getElementById("ole_num");
  ole_num.setAttribute('src','static/photos/num_b.png');
}

function simon_b() {
  simon_profile  = document.getElementById("simon_profile");
  simon_profile.setAttribute('src','static/photos/simon_b.png');

  simon_num  = document.getElementById("simon_num");
  simon_num.setAttribute('src','static/photos/num_b.png');
}

function dimi_b() {
  dimi_profile  = document.getElementById("dimi_profile");
  dimi_profile.setAttribute('src','static/photos/dimi_b.png');

  dimi_num  = document.getElementById("dimi_num");
  dimi_num.setAttribute('src','static/photos/num_b.png');
}

function morten_b() {
  morten_profile  = document.getElementById("morten_profile");
  morten_profile.setAttribute('src','static/photos/morten_b.png');

  morten_num  = document.getElementById("morten_num");
  morten_num.setAttribute('src','static/photos/num_b.png');
}

function casper_b() {
  casper_profile  = document.getElementById("casper_profile");
  casper_profile.setAttribute('src','static/photos/casper_b.png');

  casper_num  = document.getElementById("casper_num");
  casper_num.setAttribute('src','static/photos/num_b.png');
}

function chen_b() {
  chen_profile  = document.getElementById("chen_profile");
  chen_profile.setAttribute('src','static/photos/chen_b.png');

  chen_num  = document.getElementById("chen_num");
  chen_num.setAttribute('src','static/photos/num_b.png');
}

function ole_h() {
  ole_profile  = document.getElementById("ole_profile");
  ole_profile.setAttribute('src','static/photos/ole_h.png');
}

function simon_h() {
  simon_profile  = document.getElementById("simon_profile");
  simon_profile.setAttribute('src','static/photos/simon_h.png');
}

function dimi_h() {
  dimi_profile  = document.getElementById("dimi_profile");
  dimi_profile.setAttribute('src','static/photos/dimi_h.png');
}

function morten_h() {
  morten_profile  = document.getElementById("morten_profile");
  morten_profile.setAttribute('src','static/photos/morten_h.png');
}

function casper_h() {
  casper_profile  = document.getElementById("casper_profile");
  casper_profile.setAttribute('src','static/photos/casper_h.png');
}

function chen_h() {
  chen_profile  = document.getElementById("chen_profile");
  chen_profile.setAttribute('src','static/photos/chen_h.png');
}
var flag = "";
var user = "";
var max_text_temp = '';
var max_text = '';

var typeWriter_max = {
    msg: function(msg){
     return msg;
    },
    len: function(){
     return this.msg.length;
    },
    seq: 0,
    speed: 65,//打字时间(ms)
    type: function(){
     var _this = this;
     document.getElementById("Max").innerHTML = " " + _this.msg.substring(0, _this.seq);
     if (_this.seq == _this.len()) {
      _this.seq = 0;
       clearTimeout(t);
     }
     else {
      _this.seq++;
      var t = setTimeout(function(){_this.type()}, this.speed);
     }
    }
   };


function get_conv() {
            $.ajax({
                url:'/get_conv/',
                type:"GET",
                dataType:'json',
                success:function (data) {
                    $.each(data,function(k,v) {
                                // max typing
                                if (k == 'Max'){
                                    max_text = v;
                                    if (max_text != max_text_temp) {
                                        typeWriter_max.msg = max_text;
                                        typeWriter_max.type();
                                        max_text_temp = max_text;
                                    }
                                }
                                if (k == 'Status'){
                                    flag = v;
                                }
                                if (k == 'user'){
                                    user = v;
                                }
                                if (flag == 'write'){
                                    loadImage();
                                }
                                // everything is fine
                                if (k == 'Ole' && flag == 'write' ){
                                    if (v == 0) {
                                        ole_num = document.getElementById("ole_num");
                                        ole_num.setAttribute('src', '');
                                    } else if (v == 1) {
                                        ole_num = document.getElementById("ole_num");
                                        ole_num.setAttribute('src', 'static/photos/num_1.png');
                                    } else if (v == 2) {
                                        ole_num = document.getElementById("ole_num");
                                        ole_num.setAttribute('src', 'static/photos/num_2.png');
                                    } else if (v == 3) {
                                        ole_num = document.getElementById("ole_num");
                                        ole_num.setAttribute('src', 'static/photos/num_3.png');
                                    } else {
                                        ole_num = document.getElementById("ole_num");
                                        ole_num.setAttribute('src', 'static/photos/num.png');
                                    }
                                }
                                if (k == 'Simon' && flag == 'write') {
                                    if (v == 0) {
                                        simon_num = document.getElementById("simon_num");
                                        simon_num.setAttribute('src', '');
                                    } else if (v == 1) {
                                        simon_num = document.getElementById("simon_num");
                                        simon_num.setAttribute('src', 'static/photos/num_1.png');
                                    } else if (v == 2) {
                                        simon_num = document.getElementById("simon_num");
                                        simon_num.setAttribute('src', 'static/photos/num_2.png');
                                    } else if (v == 3) {
                                        simon_num = document.getElementById("simon_num");
                                        simon_num.setAttribute('src', 'static/photos/num_3.png');
                                    } else {
                                        simon_num = document.getElementById("simon_num");
                                        simon_num.setAttribute('src', 'static/photos/num.png');
                                    }
                                }
                                if (k == 'Dimi' && flag == 'write') {
                                    if (v == 0) {
                                        dimi_num = document.getElementById("dimi_num");
                                        dimi_num.setAttribute('src', '');
                                    } else if (v == 1) {
                                        dimi_num = document.getElementById("dimi_num");
                                        dimi_num.setAttribute('src', 'static/photos/num_1.png');
                                    } else if (v == 2) {
                                        dimi_num = document.getElementById("dimi_num");
                                        dimi_num.setAttribute('src', 'static/photos/num_2.png');
                                    } else if (v == 3) {
                                        dimi_num = document.getElementById("dimi_num");
                                        dimi_num.setAttribute('src', 'static/photos/num_3.png');
                                    } else {
                                        dimi_num = document.getElementById("dimi_num");
                                        dimi_num.setAttribute('src', 'static/photos/num.png');
                                    }
                                }
                                if (k == 'Morten' && flag == 'write') {
                                    if (v == 0) {
                                        morten_num = document.getElementById("morten_num");
                                        morten_num.setAttribute('src', '');
                                    } else if (v == 1) {
                                        morten_num = document.getElementById("morten_num");
                                        morten_num.setAttribute('src', 'static/photos/num_1.png');
                                    } else if (v == 2) {
                                        morten_num = document.getElementById("morten_num");
                                        morten_num.setAttribute('src', 'static/photos/num_2.png');
                                    } else if (v == 3) {
                                        morten_num = document.getElementById("morten_num");
                                        morten_num.setAttribute('src', 'static/photos/num_3.png');
                                    } else {
                                        morten_num = document.getElementById("morten_num");
                                        morten_num.setAttribute('src', 'static/photos/num.png');
                                    }
                                }
                                if (k == 'Casper' && flag == 'write') {
                                    if (v == 0) {
                                        casper_num = document.getElementById("casper_num");
                                        casper_num.setAttribute('src', '');
                                    } else if (v == 1) {
                                        casper_num = document.getElementById("casper_num");
                                        casper_num.setAttribute('src', 'static/photos/num_1.png');
                                    } else if (v == 2) {
                                        casper_num = document.getElementById("casper_num");
                                        casper_num.setAttribute('src', 'static/photos/num_2.png');
                                    } else if (v == 3) {
                                        casper_num = document.getElementById("casper_num");
                                        casper_num.setAttribute('src', 'static/photos/num_3.png');
                                    } else {
                                        casper_num = document.getElementById("casper_num");
                                        casper_num.setAttribute('src', 'static/photos/num.png');
                                    }
                                }
                                if (k == 'Chen' && flag == 'write') {
                                    if (v == 0) {
                                        chen_num = document.getElementById("chen_num");
                                        chen_num.setAttribute('src', '');
                                    } else if (v == 1) {
                                        chen_num = document.getElementById("chen_num");
                                        chen_num.setAttribute('src', 'static/photos/num_1.png');
                                    } else if (v == 2) {
                                        chen_num = document.getElementById("chen_num");
                                        chen_num.setAttribute('src', 'static/photos/num_2.png');
                                    } else if (v == 3) {
                                        chen_num = document.getElementById("chen_num");
                                        chen_num.setAttribute('src', 'static/photos/num_3.png');
                                    } else {
                                        chen_num = document.getElementById("chen_num");
                                        chen_num.setAttribute('src', 'static/photos/num.png');
                                    }
                                }

                                // highlight the reading person and blue others
                                if (k == 'Ole' && flag == 'read' && user == 'Ole'){
                                    if (v == 0) {
                                        ole_num = document.getElementById("ole_num");
                                        ole_num.setAttribute('src', 'static/photos/num_0.png');
                                    } else if (v == 1) {
                                        ole_num = document.getElementById("ole_num");
                                        ole_num.setAttribute('src', 'static/photos/num_1.png');
                                    } else if (v == 2) {
                                        ole_num = document.getElementById("ole_num");
                                        ole_num.setAttribute('src', 'static/photos/num_2.png');
                                    } else if (v == 3) {
                                        ole_num = document.getElementById("ole_num");
                                        ole_num.setAttribute('src', 'static/photos/num_3.png');
                                    } else {
                                        ole_num = document.getElementById("ole_num");
                                        ole_num.setAttribute('src', 'static/photos/num.png');
                                    }
                                //    blue others
                                    ole_h();
                                    simon_b();
                                    dimi_b();
                                    morten_b();
                                    casper_b();
                                    chen_b();
                                }
                                if (k == 'Simon' && flag == 'read' && user == 'Simon') {
                                    if (v == 0) {
                                        simon_num = document.getElementById("simon_num");
                                        simon_num.setAttribute('src', 'static/photos/num_0.png');
                                    } else if (v == 1) {
                                        simon_num = document.getElementById("simon_num");
                                        simon_num.setAttribute('src', 'static/photos/num_1.png');
                                    } else if (v == 2) {
                                        simon_num = document.getElementById("simon_num");
                                        simon_num.setAttribute('src', 'static/photos/num_2.png');
                                    } else if (v == 3) {
                                        simon_num = document.getElementById("simon_num");
                                        simon_num.setAttribute('src', 'static/photos/num_3.png');
                                    } else {
                                        simon_num = document.getElementById("simon_num");
                                        simon_num.setAttribute('src', 'static/photos/num.png');
                                    }
                                    //    blue others
                                    ole_b();
                                    simon_h();
                                    dimi_b();
                                    morten_b();
                                    casper_b();
                                    chen_b();
                                }
                                if (k == 'Dimi' && flag == 'read' && user == 'Dimi') {
                                    if (v == 0) {
                                        dimi_num = document.getElementById("dimi_num");
                                        dimi_num.setAttribute('src', 'static/photos/num_0.png');
                                    } else if (v == 1) {
                                        dimi_num = document.getElementById("dimi_num");
                                        dimi_num.setAttribute('src', 'static/photos/num_1.png');
                                    } else if (v == 2) {
                                        dimi_num = document.getElementById("dimi_num");
                                        dimi_num.setAttribute('src', 'static/photos/num_2.png');
                                    } else if (v == 3) {
                                        dimi_num = document.getElementById("dimi_num");
                                        dimi_num.setAttribute('src', 'static/photos/num_3.png');
                                    } else {
                                        dimi_num = document.getElementById("dimi_num");
                                        dimi_num.setAttribute('src', 'static/photos/num.png');
                                    }
                                    //    blue others
                                    ole_b();
                                    simon_b();
                                    dimi_h();
                                    morten_b();
                                    casper_b();
                                    chen_b();
                                }
                                if (k == 'Morten' && flag == 'read' && user == 'Morten') {
                                    if (v == 0) {
                                        morten_num = document.getElementById("morten_num");
                                        morten_num.setAttribute('src', 'static/photos/num_0.png');
                                    } else if (v == 1) {
                                        morten_num = document.getElementById("morten_num");
                                        morten_num.setAttribute('src', 'static/photos/num_1.png');
                                    } else if (v == 2) {
                                        morten_num = document.getElementById("morten_num");
                                        morten_num.setAttribute('src', 'static/photos/num_2.png');
                                    } else if (v == 3) {
                                        morten_num = document.getElementById("morten_num");
                                        morten_num.setAttribute('src', 'static/photos/num_3.png');
                                    } else {
                                        morten_num = document.getElementById("morten_num");
                                        morten_num.setAttribute('src', 'static/photos/num.png');
                                    }
                                    //    blue others
                                    ole_b();
                                    simon_b();
                                    dimi_b();
                                    morten_h();
                                    casper_b();
                                    chen_b();
                                }
                                if (k == 'Casper' && flag == 'read' && user == 'Casper') {
                                    if (v == 0) {
                                        casper_num = document.getElementById("casper_num");
                                        casper_num.setAttribute('src', 'static/photos/num_0.png');
                                    } else if (v == 1) {
                                        casper_num = document.getElementById("casper_num");
                                        casper_num.setAttribute('src', 'static/photos/num_1.png');
                                    } else if (v == 2) {
                                        casper_num = document.getElementById("casper_num");
                                        casper_num.setAttribute('src', 'static/photos/num_2.png');
                                    } else if (v == 3) {
                                        casper_num = document.getElementById("casper_num");
                                        casper_num.setAttribute('src', 'static/photos/num_3.png');
                                    } else {
                                        casper_num = document.getElementById("casper_num");
                                        casper_num.setAttribute('src', 'static/photos/num.png');
                                    }
                                    //    blue others
                                    ole_b();
                                    simon_b();
                                    dimi_b();
                                    morten_b();
                                    casper_h();
                                    chen_b();
                                }
                                if (k == 'Chen' && flag == 'read' && user == 'Chen') {
                                    if (v == 0) {
                                        chen_num = document.getElementById("chen_num");
                                        chen_num.setAttribute('src', 'static/photos/num_0.png');
                                    } else if (v == 1) {
                                        chen_num = document.getElementById("chen_num");
                                        chen_num.setAttribute('src', 'static/photos/num_1.png');
                                    } else if (v == 2) {
                                        chen_num = document.getElementById("chen_num");
                                        chen_num.setAttribute('src', 'static/photos/num_2.png');
                                    } else if (v == 3) {
                                        chen_num = document.getElementById("chen_num");
                                        chen_num.setAttribute('src', 'static/photos/num_3.png');
                                    } else {
                                        chen_num = document.getElementById("chen_num");
                                        chen_num.setAttribute('src', 'static/photos/num.png');
                                    }
                                    //    blue others
                                    ole_b();
                                    simon_b();
                                    dimi_b();
                                    morten_b();
                                    casper_b();
                                    chen_h();
                                }


                    })
                }
            })
        };


setInterval(get_conv,1000);