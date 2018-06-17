import Vue from 'vue'
import Vuetify from 'vuetify'
import App from './App'
import store from './store.js'
import router from './router.js'

import 'vuetify/dist/vuetify.min.css'

Vue.use(Vuetify)

Vue.config.productionTip = false

new Vue({
    el: '#app',
    store,
    router,
    components: { App },
    template: '<App/>'
})
