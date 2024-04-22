const wrapper=document.querySelector('.wrapper')
const register_link=document.querySelector('.register-link')
const login_link=document.querySelector('.login-link')


register_link.onclick = () =>
{
    wrapper.classList.add('active');
}

login_link.onclick = () =>
{
    wrapper.classList.remove('active');
}