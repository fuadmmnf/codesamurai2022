<template>
      <div style="height: 100vh; width: 100%;" ref="ganttContainer"></div>
</template>

<script>
import {gantt} from 'dhtmlx-gantt';

export default {
  name: "Gantt",
  data () {
    return {
      tasks: {
        data: [
          {id: 1, text: 'Task #1', start_date: '2020-01-17', duration: 3, progress: 0.6},
          {id: 2, text: 'Task #2', start_date: '2020-01-20', duration: 3, progress: 0.4}
        ],
        links: [
          {id: 1, source: 1, target: 2, type: '0'}
        ]
      },
    }
  },
  mounted: function () {
    gantt.config.date_format = "%Y-%m-%d";

    gantt.init(this.$refs.ganttContainer);
    gantt.parse(this.tasks);
  }
}
</script>

<style>
@import "~dhtmlx-gantt/codebase/dhtmlxgantt.css";
.container {
  height: 100vh;
  width: 100%;
}
.left-container {
  overflow: hidden;
  position: relative;
  height: 100%;
}
</style>
