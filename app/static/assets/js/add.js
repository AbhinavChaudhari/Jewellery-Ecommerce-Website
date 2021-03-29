
var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product 
        var action = this.dataset.action
        // var user = request.user
        console.log('productId:',productId,action,);
        // console.log("user",user);
        if (user ==="AnonymousUser"){
            console.log("user is AnonymousUser");
        }else{
            addToCart(productId,action)
        }
    })
}

function addToCart(productId,action){
    
    $.ajax({
        type: "POST",
        url: "/updateItem/",
        headers:{"X-CSRFToken":getCookie('csrftoken')},
        data:{data:JSON.stringify({'productId':productId,'action':action})},
        dataType: 'json',
        success: function (data) {
           alert(data.msg)
           
        //    Notiflix.Notify.Success('Sol lucet omnibus');
         },
       
        
    })
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



var citiesByState = {
Odisha: ["Bhubaneswar","Puri","Cuttack"],
Maharashtra: ["Mumbai","Pune","Nagpur"],
Kerala: ["kochi","Kanpur"]
}
function makeSubmenu(value) {
if(value.length==0) document.getElementById("citySelect").innerHTML = "<option></option>";
else {
var citiesOptions = "";
for(cityId in citiesByState[value]) {
citiesOptions+="<option>"+citiesByState[value][cityId]+"</option>";
}
document.getElementById("citySelect").innerHTML = citiesOptions;
}
}
function displaySelected() { var country = document.getElementById("countrySelect").value;
var city = document.getElementById("citySelect").value;
alert(country+"\n"+city);
}
function resetSelection() {
document.getElementById("countrySelect").selectedIndex = 0;
document.getElementById("citySelect").selectedIndex = 0;
}

