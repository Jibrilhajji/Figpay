import Ember from 'ember';
import defaultTheme from '../../themes/default-theme';
export default Ember.Component.extend({
  
  chartOptions: {
    chart: {
      type: 'bar'
    },
    title: {
      text: 'Month Breakdown'
    },
    xAxis: {
      categories: ['January', 'February', 'March','April','May','June','July','August','September','October','November','December']
    },
    yAxis: {
      title: {
        text: 'Money spent'
      }
    }
  },
  theme: defaultTheme,
  chartData: [
    {
      
      data: [320,400,203,549,293,548,391,567,129,200,390,450]
    },
  ],
});
