<template>
<div id="vaccine">
    <table class="table" border="1">
      <th class="vacc" colspan="6">백신 현황</th>
      <tr>
        <th>지역</th>
        <th>총 인구 수</th>
        <th>1차 접종</th>
        <th>1차접종률</th>
        <th>접종완료</th>
        <th>접종완료접종률</th>
      </tr>
        <td><span>{{this.vaccine.placeinfo}}</span></td>
        <td><span>{{this.vaccine.peoplenum}}</span></td>
        <td><span>{{this.vaccine.firstnum}}</span></td>
        <td><span>{{this.vaccine.vaccine.firstpernum}}%</span></td>
        <td><span>{{this.vaccine.secnum}}</span></td>
        <td><span>{{this.vaccine.secpernum}}%</span></td>
    </table>
    <section class="container12">
      <div class="column2">
        <bar-chart></bar-chart>
      </div>
  </section>
  </div>
</template>

<script>
import BarChart from '@/views/BarChart'
import axios from "axios"
export default {
  name: "vaccine",
    components: {
      BarChart,
    },
    data() {
      return {
        vaccine: []
      };
    },
    async created() {
      try {
        const res = await axios.get('/vaccine');
        this.vaccine = res.data;
      } 
      catch (e) {
        console.error(e);
      }
    }
};
</script>

<style>
.vacc {
  font-size: 1.6em;
  background-color: rgb(212, 212, 248);
}
.table {
    display: inline-block;
    height: 168px;
    border: 1px solid rgba(0, 0, 0, 0);
    color: black;
    background: rgba(255, 255, 255, 0);
    margin-top: 10px;
    margin-left: 1px;
}
td, th {
  width: 1200px;
  height: 40px;
  padding: 1px;
  border: 1px solid rgb(5, 5, 5);
  font-size: 1.6em;
}
th {
  background-color: rgb(233, 255, 199);
}
td {
  background-color: rgb(219, 211, 211);
}
body {
  padding: 1rem;
}
.container2 {
  margin-left: 74px;
  margin-top: -320px;
}
.column2 {
    display: inline-block;
    width: 1300px;
    height: 440px;
    border: 1px solid rgba(0, 0, 0, 0);
    color: black;
    background: rgba(255, 255, 255, 0);
    margin-right: -20px;
    margin-top: -10px;
    margin-bottom: -1px;
}
</style>