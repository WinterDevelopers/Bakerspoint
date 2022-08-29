let footer_img = document.querySelectorAll('[name="footer-img"]')
let footer_p_item = document.querySelectorAll('[name="footer-dropdown"]')

let mobile_menu_btn = document.querySelector('#mobile-menu-btn')
let mobile_menu = document.querySelector('#mobile-menu')
let mobile_menu_cancel_btn = document.querySelector('#mobile-menu-cancel-btn')

mobile_menu_btn.addEventListener('click',function(){
    mobile_menu.className='mobile-menu no-display-menu'
})
mobile_menu_cancel_btn.addEventListener('click', function(){
    mobile_menu.className='mobile-menu-cancel'
})

for(let a = 0; a < footer_img.length; a++){

    footer_img[a].addEventListener("click", function(){
        if(footer_img[a].className !='rotate-90'){
            footer_img[a].className = 'rotate-90'
            footer_p_item[a].className = 'footer-content-p-animate footer-content-p'
        }else{
            footer_img[a].className = 'reverse-rotate-90'
            footer_p_item[a].className = 'no-display-min-animate'
            
        }
    })
}
