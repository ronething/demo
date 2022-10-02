<template>
  <div>
    <h1>详情页</h1>
    <p>{{ message }}</p>
    <router-link to="/">返回首页</router-link>
  </div>
</template>

<script>
  export default {
    name: "Detail",
    data() {
      return {
        message: ""
      }
    },
    mounted() {
      // let uuid = this.$route.params.uuid;
      let api_url = "http://xxx.ronething.com";
      this.axios.get(api_url + "/web/" + this.$route.params.uuid)
        .then(body => {
          // console.log(body.data);
          let code = body.data.code;
          if (code === 200) {
            this.message = body.data.data.text;
          } else {
            this.message = body.data.message;
          }
        })
        .catch(error => {
          // console.log(error.data);
          this.message = "烂了 你懂吧"
        })
    }
  }
</script>

<style scoped>

</style>
