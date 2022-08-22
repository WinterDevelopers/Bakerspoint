console.log('Bakerspoint')

let footer_img = document.querySelectorAll('[name="footer-img"]')
let footer_p_item = document.querySelectorAll('[name="footer-dropdown"]')
console.log(footer_p_item)

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

console.log('done!!')