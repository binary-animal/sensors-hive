import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import Login from '@/components/Login'
import Entrance from '@/components/Entrance'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'Entrance',
            component: Entrance
        },
        {
            path: '/main',
            name: 'Main',
            component: Main
        },
        {
            path: '/login',
            name: 'Login',
            component: Login
        }
    ]
})
