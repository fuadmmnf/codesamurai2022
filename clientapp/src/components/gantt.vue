<template>
  <div style="height: 100vh; width: 100%;" ref="ganttContainer"></div>
</template>

<script>
import {gantt} from 'dhtmlx-gantt';
import {api} from "boot/axios";

export default {
  name: "Gantt",
  props: {
    project_id: {
      type: String,
      required: true
    },
  },
  data() {
    return {
      tasks: {
        data: [
          // {id: 1, text: 'Task #1', start_date: '2020-01-17', duration: 3, progress: 0.6},
          // {id: 2, text: 'Task #2', start_date: '2020-01-20', duration: 3, progress: 0.4}
        ]
      },
    }
  },
  mounted: function () {
    api.get(`projects/${this.project_id}/components`).then((response) => {
      console.log(response.data.data)
      response.data.data.forEach((element) => {
        let temp = {
          id: element.id,
          text: element.component_id,
          start_date: '2020-01-17',
          duration: 3,
          progress: 0.0
        }
        this.tasks.data.push(temp)
        gantt.config.date_format = "%Y-%m-%d";
        gantt.init(this.$refs.ganttContainer);
        gantt.parse(this.tasks);
      })
    })
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
