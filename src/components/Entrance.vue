<template>
    <div></div>
</template>

<script>

export default {

    name: 'Entrance',

    mounted: function () {
        this.$nextTick(function () {
            if (this.$store.state.user.login == 'guest') {
                this.$router.push('/Login');
            } else {
                this.$router.push('/Main');
            }
        })
    }

}

</script>
