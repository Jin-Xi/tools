<template>
    <div class="test-container">
        <div class="flex-col wrapper">
            <span class="user-nickname">用户昵称:</span>
            <div class="flex-row wraper-row">
                <div class="flex-col flex-row box">
                    <span class="user-nickname-two">用户昵称:</span>
                    <div class="box-row"></div>
                    <div class="box-row-two"></div>
                </div>
                <div class="flex-col flex-row box-two">
                    <div class="box-row-three"></div>
                    <div class="box-row-four"></div>
                </div>
            </div>
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
<style>
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
        padding: 32px 0px 45px 76px;
    }

    .test-container .wrapper .user-nickname {
        margin: 0px 0px 14px 437px;
        font-size: 14px;
        line-height: 14px;
    }

    .test-container .wrapper .wraper-row {
        width: 618px;
        justify-content: space-between;
    }

    .test-container .wrapper .box {
        width: 262px;
        margin-top: 38px;
    }

    .test-container .wrapper .user-nickname-two {
        margin: 0px 0px 40px 93px;
        font-size: 14px;
        line-height: 14px;
    }

    .test-container .wrapper .box-row {
        width: 100%;
        height: 246px;
        margin-bottom: 47px;
    }

    .test-container .wrapper .box-row-two {
        width: 146px;
        height: 42px;
        margin-right: auto;
        margin-left: auto;
    }

    .test-container .wrapper .box-two {
        width: 297px;
    }

    .test-container .wrapper .box-row-three {
        width: 292px;
        height: 216px;
        margin-bottom: 33px;
    }

    .test-container .wrapper .box-row-four {
        width: 292px;
        height: 216px;
        margin-left: 5px;
    }
</style>
