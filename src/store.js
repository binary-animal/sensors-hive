import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import VueAxios from 'vue-axios'
import router from './router.js'

Vue.use(VueAxios, axios)
Vue.use(Vuex)

export default new Vuex.Store({

    state: {

        user: {
            id: 0,
            login: 'guest',
            password: '',
            token: '',
        },

        page: 'entrance',

    },

    mutations: {

        LOGIN: function(state, user) {
            state.user = user;
            router.push('/Main');
        }

    },

    actions: {

        login: function (context, creadentials) {
            axios.post('/api/login', creadentials).then(response => {
                context.commit('LOGIN', response.data.data);
            });
        },

    }

})
