
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
            alert("Login First ")
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
    $.ajax({
        type:"GET",
        url:"/getCartQty/",
        success:function (response) {

           if(response.cart.length == 0){
             
             console.log('cart disabled');
           }else{
                var cart = response.cart.length
                document.getElementById('cartvalue').innerHTML = cart
                document.getElementById('mobilecart').innerHTML = cart
           }
        }
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




