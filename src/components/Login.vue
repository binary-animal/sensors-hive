<template>
    <v-app>
        <v-layout justify-center>
            <v-flex xs4 sm4 md4 lg4>
                <v-card ref="form">
                    <v-card-text>
                        <v-text-field
                        ref="login"
                        label="Login"
                        placeholder="Login"
                        v-model="login"
                        required
                        ></v-text-field>
                        <v-text-field
                        type="password"
                        ref="password"
                        label="Password"
                        v-model="password"
                        required
                        ></v-text-field>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" @click="doLogin">Login</v-btn>
                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
    </v-app>
</template>

<script>

export default {

    name: 'Login',

    data () {

        return {
            login: '',
            password: ''
        }

    },

    methods: {
        doLogin: function() {
            this.$store.dispatch('login', {login: this.login, password: this.password});
        }
    }

}

</script>
