<template>
    <div class="test-container">
        <div class="flex-col wrapper">
            <div class="flex-row wraper-row">
                <span class="user-nickname">用户昵称:</span><span class="user-nickname">用户昵称:</span>
            </div>
            <div class="flex-row wraper-row-two">
                <div class="box">
                    <img class="img" src="https://vkceyugu.cdn.bspapp.com/VKCEYUGU-55dbb834-9ba8-4068-98ca-c341f6402e27/38f6a050-ae91-436f-825b-9f751d5d9019.png" />
                </div>
                <div class="box-two">
                    <img class="img-two" src="https://vkceyugu.cdn.bspapp.com/VKCEYUGU-55dbb834-9ba8-4068-98ca-c341f6402e27/38f6a050-ae91-436f-825b-9f751d5d9019.png" />
                </div>
            </div>
            <div class="wraper-row-three"></div>
            <div class="wraper-row-four"></div>
        </div>
    </div>
</template>
<script>
    export default {
        data() {
            return {}
        },
        methods: {

        }
    }
</script>
<style scoped>
    /** 全局样式-开始,建议放在公共css样式文件中,比如common.css 或app.vue文件 */

    html,
    body {
        margin: 0;
        width: 100%;
        height: 100%;
        font-size: 16px
    }

    * {
        position: relative;
        box-sizing: border-box;
        flex-shrink: 0;
    }

    .flex-col {
        display: flex;
        align-items: flex-start;
        flex-direction: column;
    }

    .flex-row {
        display: flex;
        align-items: flex-start;
    }

    .flex-col .flex-row {
        width: 100%
    }

    /** 全局样式-结束*/

    .test-container {
        padding: 110px 0px 119px 128px;
    }

    .test-container .wrapper {
        width: 760px;
        height: 570px;
        padding: 46px 0px 0px 76px;
    }

    .test-container .wrapper .wraper-row {
        width: 392px;
        justify-content: space-between;
        margin: 0px 0px 12px 83px;
    }

    .test-container .wrapper .user-nickname {
        font-size: 14px;
        line-height: 14px;
    }

    .test-container .wrapper .wraper-row-two {
        width: 555px;
        justify-content: space-between;
        margin-bottom: 42px;
    }

    .test-container .wrapper .box {
        width: 226px;
        height: 214px;
        margin-top: 2px;
    }

    .test-container .wrapper .img {
        width: 222px;
        height: 209px;
    }

    .test-container .wrapper .box-two {
        width: 218px;
        padding: 6px 0px 6px 1px;
    }

    .test-container .wrapper .img-two {
        width: 212px;
        height: 204px;
    }

    .test-container .wrapper .wraper-row-three {
        width: 286px;
        height: 51px;
        margin: 0px 0px 31px 131px;
    }

    .test-container .wrapper .wraper-row-four {
        width: 146px;
        height: 42px;
        margin-left: 201px;
    }
</style>
