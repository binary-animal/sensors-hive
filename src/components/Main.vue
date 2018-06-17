<template>
    <v-app>
        <v-layout>
            <v-flex xs12 sm6 offset-sm3>
                <v-card>
                    <v-card-title primary-title>
                        <div>User id: {{ id }}</div>
                        <div>User login: {{ login }}</div>
                        <div>User token: {{ token }}</div>
                    </v-card-title>
                </v-card>
            </v-flex>
        </v-layout>
    </v-app>
</template>

<script>

export default {
    name: 'Main',

    computed: {
        id: function() {
            return this.$store.state.user.id
        },
        login: function() {
            return this.$store.state.user.login
        },
        token: function() {
            return this.$store.state.user.token
        }
    }

}

</script>
