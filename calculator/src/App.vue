<template>
  <div id="app" class="calculator-app container">
    <div class="screen display">
      <div class="old-data"></div>
      <div class="new-data">{{current || '0'}}</div>
    </div>
    <div class="keypad">
      <div @click="sign" class="btn">+/-</div>
      <div class="btn operator">( )</div><!--@click="bracket"-->
      <div @click="percent" class="btn">%</div>
      <div @click="divide" class="btn operator">/</div>

      <div @click="append('7')" class="btn num">7</div>
      <div @click="append('8')" class="btn num">8</div>
      <div @click="append('9')" class="btn num">9</div>
      
      <div @click="multiply" class="btn operator">x</div>

      <div @click="append('4')" class="btn num">4</div>
      <div @click="append('5')" class="btn num">5</div>
      <div @click="append('6')" class="btn num">6</div>

      <div @click="subtract" class="btn operator">-</div>

      <div @click="append('1')" class="btn num">1</div>
      <div @click="append('2')" class="btn num">2</div>
      <div @click="append('3')" class="btn num">3</div>

      <div @click="add" class="btn operator">+</div>
      <div @click="clear" class="btn">C</div>
      <div @click="append('0')" class="btn num">0</div>
      <div @click="decimal" class="btn">.</div>
      <div @click="solve" class="btn">=</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return{
      current: '',
      operator: null,
      previous: null,
      operator_clicked: false,
      value: '',
    }    
  },
  methods:{
    // clear the screen
    clear(){
      this.current = '';
    },

    // convert to neg or pos value
    sign(){
      this.current = this.current.charAt(0) === '-' ? this.current.slice(1): `-${this.current}`;
    },

    // convert to percentage value
    percent(){
      this.current = `${parseFloat(this.current) / 100}`;
    },

    // convert to neg or pos value
    // bracket(){
    //   this.current = this.current.charAt(0) === '-' ? this.current.slice(1): `-${this.current}`;
    // },

    // convert to neg or pos value
    decimal(){
      this.current = this.current.isInteger() ? `${this.current}.`: this.current;
    },
    append(number){
      if(this.operator_clicked){
        this.current = '';
        this.operator_clicked = false;
      }
      this.current = `${this.current}${number}`

    },

    // convert to neg or pos value
    solve(){
      // get final answer
      this.current = this.operator(
        parseFloat(this.current),
        parseFloat(this.previous)
      );
      this.previous = null;

    },
    divide(){
      this.operator = (prev, next) => prev/next;
      this.value = '/'
      this.previous = this.current;
      this.operator_clicked = true;
    },
    add(){
      this.operator = (prev, next) => prev+next;
      this.value = '+'
      this.previous = this.current;
      this.operator_clicked = true;
    },
    multiply(){
      this.operator = (prev, next) => prev*next;
      this.value = '*'
      this.previous = this.current;
      this.operator_clicked = true;
    },
    subtract(){
      this.operator = (prev, next) => prev-next;
      this.value = '-'
      this.previous = this.current;
      this.operator_clicked = true;
    },
    showfeed(){
    }
  }
}

</script>



<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600&display=swap');
.keypad{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: minmax(50px, auto);
  padding-top: 5px;
}
.btn{
  cursor: pointer;
  border-radius: 20px;
  border: 1px solid rgba(90, 84, 84, 0.863);
  margin: 1px;
  font-size: 30px;
  font-weight: 500;
  text-align: center;
  padding: 10% 0;
  font-family: 'Orbitron', sans-serif;
}
.display{
  border: 1px solid rgba(90, 84, 84, 0.863);
  height: 100px;
  text-align-last: right;
  overflow: hidden;
  font-family: 'Orbitron', sans-serif;
}
.container{
  width: 300px;
  margin: 0 auto;
}

.new-data, .old-data{
  /* border: 2px solid black; */
  height: 50%;
  font-size: 30px;
}

/* .operator{
  background-color: #fff;
} */

</style>
