<template>
  <div>
    <h1>阅后即焚</h1>
    <div class="container">
      <p>Message is: {{ message }}</p>
      <p>url is: {{ url }}
        {{ status }}
        <button type="button" class="btn-info btn" @click="doCopy">Copy</button>
        <button type="button" class="btn btn-info" @click="getUrl">Generate</button>
      </p>
      <!--<router-link :to="url" class="btn-info">右键可以复制链接</router-link>-->
    </div>
    <div class="container">
      <div class="form-group">
        <textarea class="form-control" v-model="message" placeholder="体验阅后即焚……" rows="6"></textarea>
      </div>
    </div>

  </div>
</template>

<script>
  export default {
    name: "Home",
    data() {
      return {
        message: "",
        url: "",
        status: "",
      }
    },
    watch: {
      message: function () {
        this.url = "";
        this.status = "";
      }
    },
    methods: {
      getUrl() {
        let api_url = "http://xxx.ronething.com";
        this.axios.post(api_url + "/web/generate", {
          text: this.message
        })
          .then(body => {
            // console.log(body.data);
            this.url = body.data.data.uuid;
            this.status = "";
          })
          .catch(error => {
            console.log(error.data);
            this.url = "烂了 你懂吧"
            this.status = "";
          });
      },
      doCopy: function () {
        // let base_url = window.location.href;
        let base_url = "http://xxx.ronething.com/#/";
        let copy_url = base_url + this.url;
        this.$copyText(copy_url).then(e => {
          // alert('Copied');
          this.status = " Copied"
          // console.log(e)
        }, e => {
          // alert('Can not copy');
          this.status = " Can not copy";
          // console.log(e)
        })
      }
    }
  }
</script>

<style scoped>

</style>
