// -*- coding: utf-8 -*-
// :Project:   SoL — Match digital scorecard
// :Created:   gio 22 dic 2022, 08:36:15
// :Author:    Lele Gaifax <lele@metapensiero.it>
// :License:   GNU General Public License version 3 or later
// :Copyright: © 2022, 2023 Lele Gaifax
//

//jsl:declare $

class MatchScorecard {
  constructor(breaker, max_allowed_boards, duration, pre_alarm, elapsed) {
    this.breaker = breaker;
    this.max_allowed_boards = max_allowed_boards;
    this.duration = duration;
    if(elapsed !== false && elapsed < 1000 * 60 * duration) {
      this.started_at = Date.now() - elapsed;
      this.pre_alarm_at = this.started_at + 1000 * 60 * (duration - pre_alarm);
    } else {
      this.started_at = false;
      this.pre_alarm_at = false;
    }
  }

  get played_boards_count() {
    return document.querySelectorAll('form > table > tbody > tr').length - 1;
  }

  get countdown() {
    const started_at = this.started_at,
          pre_alarm_at = this.pre_alarm_at,
          now = Date.now(),
          progress = now - started_at,
          left = this.duration - (progress / 1000 / 60),
          mins = Math.trunc(left),
          secs = Math.trunc((left-mins)*60);
    return { mins, secs, pre_alarm: pre_alarm_at && pre_alarm_at < now };
  }

  new_board_row(board, c1_break_classes, c2_break_classes) {
    // <tr id="board_${board}">
    //   <td class="center aligned ${c1_break_classes}" id="score_${board}_1"></td>
    //   <td class="center aligned">
    //     <div class="field">
    //       <input type="number" name="coins_${board}_1" min="0" max="9">
    //     </div>
    //   </td>
    //   <td class="collapsing">
    //     <div class="field">
    //       <div class="ui radio checkbox center aligned" id="cb_queen_${board}_1">
    //         <input type="radio" name="queen_${board}" value="1">
    //       </div>
    //     </div>
    //   </td>
    //   <td class="grey center aligned collapsing" colspan="2">${board}</td>
    //   <td class="collapsing">
    //     <div class="field">
    //       <div class="ui radio checkbox center aligned" id="cb_queen_${board}_2">
    //         <input type="radio" name="queen_${board}" value="2">
    //       </div>
    //     </div>
    //   </td>
    //   <td class="center aligned">
    //     <div class="field">
    //       <input type="number" name="coins_${board}_2" min="0" max="9">
    //     </div>
    //   </td>
    //   <td class="center aligned ${c2_break_classes}" id="score_${board}_2"></td>
    // </tr>;

    var tr = document.createElement('tr');
    tr.id = `board_${board}`;

    var score_c1 = document.createElement('td');
    score_c1.id = `score_${board}_1`;
    score_c1.className = 'center aligned';
    if(c1_break_classes) score_c1.classList.add(...c1_break_classes);
    tr.appendChild(score_c1);

    var coins_c1 = document.createElement('td');
    coins_c1.className = 'center aligned';

    var coins_c1_field = document.createElement('div');
    coins_c1_field.className = 'field';

    var coins_c1_input = document.createElement('input');
    coins_c1_input.setAttribute('type', 'number');
    coins_c1_input.setAttribute('name', `coins_${board}_1`);
    coins_c1_input.setAttribute('min', '0');
    coins_c1_input.setAttribute('max', '9');
    coins_c1_field.appendChild(coins_c1_input);
    coins_c1.appendChild(coins_c1_field);
    tr.appendChild(coins_c1);

    var queen_c1 = document.createElement('td');
    queen_c1.className = 'collapsing';

    var queen_c1_field = document.createElement('div');
    queen_c1_field.className = 'field';

    var queen_c1_radio = document.createElement('div');
    queen_c1_radio.id = `cb_queen_${board}_1`;
    queen_c1_radio.className = 'ui radio checkbox center aligned';

    var queen_c1_input = document.createElement('input');
    queen_c1_input.setAttribute('type', 'radio');
    queen_c1_input.setAttribute('name', `queen_${board}`);
    queen_c1_input.setAttribute('value', '1');
    queen_c1_radio.appendChild(queen_c1_input);
    queen_c1_field.appendChild(queen_c1_radio);
    queen_c1.appendChild(queen_c1_field);
    tr.appendChild(queen_c1);

    var middle_col = document.createElement('td');
    middle_col.className = 'grey center aligned collapsing';
    middle_col.setAttribute('colspan', '2');
    middle_col.append(board);
    tr.appendChild(middle_col);

    var queen_c2 = document.createElement('td');
    queen_c2.className = 'collapsing';

    var queen_c2_field = document.createElement('div');
    queen_c2_field.className = 'field';

    var queen_c2_radio = document.createElement('div');
    queen_c2_radio.id = `cb_queen_${board}_2`;
    queen_c2_radio.className = 'ui radio checkbox center aligned';

    var queen_c2_input = document.createElement('input');
    queen_c2_input.setAttribute('type', 'radio');
    queen_c2_input.setAttribute('name', `queen_${board}`);
    queen_c2_input.setAttribute('value', '2');
    queen_c2_radio.appendChild(queen_c2_input);
    queen_c2_field.appendChild(queen_c2_radio);
    queen_c2.appendChild(queen_c2_field);
    tr.appendChild(queen_c2);

    var coins_c2 = document.createElement('td');
    coins_c2.className = 'center aligned';

    var coins_c2_field = document.createElement('div');
    coins_c2_field.className = 'field';

    var coins_c2_input = document.createElement('input');
    coins_c2_input.setAttribute('type', 'number');
    coins_c2_input.setAttribute('name', `coins_${board}_2`);
    coins_c2_input.setAttribute('min', '0');
    coins_c2_input.setAttribute('max', '9');
    coins_c2_field.appendChild(coins_c2_input);
    coins_c2.appendChild(coins_c2_field);
    tr.appendChild(coins_c2);

    var score_c2 = document.createElement('td');
    score_c2.id = `score_${board}_2`;
    score_c2.className = 'center aligned';
    if(c2_break_classes) score_c2.classList.add(...c2_break_classes);
    tr.appendChild(score_c2);

    return tr;
  }

  add_board() {
    const self = this,
          new_board = self.played_boards_count + 1;
    var c1_break_classes = null,
        c2_break_classes = null;

    if(!self.breaker) {
      if(document.querySelector('input[name="breaker"][value="1"]').checked)
        self.breaker = 1;
      else if(document.querySelector('input[name="breaker"][value="2"]').checked)
        self.breaker = 2;
    }

    if(self.breaker) {
      const c1 = document.querySelector('tr th:first-child'),
            c2 = document.querySelector('tr th:last-child');

      if(self.breaker === 1) {
        if(new_board % 2) {
          c1_break_classes = ['left', 'red', 'marked'];
          c1.classList.add('current-breaker');
          c2.classList.remove('current-breaker');
        } else {
          c2_break_classes = ['right', 'red', 'marked'];
          c1.classList.remove('current-breaker');
          c2.classList.add('current-breaker');
        }
      } else {
        if(new_board % 2) {
          c2_break_classes = ['right', 'red', 'marked'];
          c1.classList.remove('current-breaker');
          c2.classList.add('current-breaker');
        } else {
          c1_break_classes = ['left', 'red', 'marked'];
          c1.classList.add('current-breaker');
          c2.classList.remove('current-breaker');
        }
      }
    }

    const row = self.new_board_row(new_board, c1_break_classes, c2_break_classes);
    document.getElementById('totals').before(row);

    self.recompute_scores_and_totals_on_change(new_board);
    document.querySelectorAll('div.checker').forEach((div) => {
      div.style.display = 'none';
    })
    document.getElementById('new_board_btn').classList.add('disabled');
  }

  recompute_scores_and_totals_on_change(board) {
    const self = this,
          board_row = document.getElementById(`board_${board}`),
          names = [`coins_${board}_1`, `coins_${board}_2`, `queen_${board}`];

    names.forEach((name) => {
      board_row.querySelectorAll(`input[name="${name}"]`).forEach((input) => {
        input.addEventListener('keyup', (event) => {
          self.compute_scores_and_totals(name);
        });
        input.addEventListener('change', (event) => {
          self.compute_scores_and_totals(name);
        });
        if(name.startsWith('coins')) {
          input.addEventListener('focus', (event) => {
            input.select();
          });
        }
      });
    });
  }

  compute_scores_and_totals(what_changed) {
    const boards = this.played_boards_count,
          new_board_btn = document.getElementById('new_board_btn'),
          end_game_btn = document.getElementById('end_game_btn');

    if(what_changed && what_changed.startsWith('coins')) {
      var coins = document.querySelector(`input[name="${what_changed}"]`).value;
      // We where triggered by an user change
      if(coins !== '') {
        const other_coins = what_changed.slice(0, -1) + (what_changed.endsWith('1') ? '2' : '1');
        document.querySelector(`input[name="${other_coins}"]`).value = 0;
      }
    }

    var total_1 = 0,
        total_2 = 0,
        last_ok = false;

    for(var board = 1; board <= boards; board++) {
      const coins_1_input = document.querySelector(`input[name="coins_${board}_1"]`),
            coins_2_input = document.querySelector(`input[name="coins_${board}_2"]`),
            coins_1 = coins_1_input.value,
            coins_2 = coins_2_input.value,
            queen_1_input = document.getElementById(`cb_queen_${board}_1`).firstElementChild,
            queen_2_input = document.getElementById(`cb_queen_${board}_2`).firstElementChild,
            queen_1 = queen_1_input.checked,
            queen_2 = queen_2_input.checked;
      var score_1 = parseInt(coins_1) || 0,
          score_2 = parseInt(coins_2) || 0;

      if(score_1 > 9)
        coins_1_input.parentElement.classList.add('error');
      else
        coins_1_input.parentElement.classList.remove('error');

      if(score_2 > 9)
        coins_2_input.parentElement.classList.add('error');
      else
        coins_2_input.parentElement.classList.remove('error');

      if(score_1 > 9 || score_2 > 9) {
        new_board_btn.classList.add('disabled');
        end_game_btn.classList.add('disabled');
        return;
      } else {
        new_board_btn.classList.remove('disabled');
        end_game_btn.classList.remove('disabled');
      }
      // Did one of the player commit suicide? Check for an explicit '0' being entered
      if(coins_1 === '0' && coins_2 === '0') {
        if(queen_1)
          score_1 += total_1 < 22 ? 3 : 1;
        else if(queen_2)
          score_2 += total_2 < 22 ? 3 : 1;
      } else {
        if(queen_1 && score_1 > score_2 && total_1 < 22)
          score_1 += 3;
        else if(queen_2 && score_1 < score_2 && total_2 < 22)
          score_2 += 3;
      }

      const s1 = document.getElementById(`score_${board}_1`),
            s2 = document.getElementById(`score_${board}_2`);

      if(score_1 > score_2) {
        s1.classList.add('positive');
        s1.classList.remove('negative');
        s2.classList.add('negative');
        s2.classList.remove('positive');
      } else if(score_1 < score_2) {
        s1.classList.add('negative');
        s1.classList.remove('positive');
        s2.classList.add('positive');
        s2.classList.remove('negative');
      } else {
        s1.classList.add('positive');
        s1.classList.remove('negative');
        s2.classList.add('positive');
        s2.classList.remove('negative');
      }
      s1.innerText = score_1;
      s2.innerText = score_2;
      total_1 += score_1;
      total_2 += score_2;

      last_ok = coins_1 !== '' && coins_2 !== '' && (queen_1 || queen_2);
    }

    if(total_1 > 25) total_1 = 25;
    if(total_2 > 25) total_2 = 25;

    document.querySelector('input[name="score1"]').value = total_1;
    document.querySelector('input[name="score2"]').value = total_2;

    const t1 = document.getElementById('total_1'),
          t2 = document.getElementById('total_2');

    t1.innerHTML = `<big><strong>${total_1}</strong></big>`;
    t2.innerHTML = `<big><strong>${total_2}</strong></big>`;

    if(total_1 > total_2) {
      t1.classList.add('positive');
      t1.classList.remove('negative');
      t2.classList.add('negative');
      t2.classList.remove('positive');
    } else if(total_1 < total_2) {
      t1.classList.add('negative');
      t1.classList.remove('positive');
      t2.classList.add('positive');
      t2.classList.remove('negative');
    } else {
      t1.classList.add('positive');
      t1.classList.remove('negative');
      t2.classList.add('positive');
      t2.classList.remove('negative');
    }

    // Is last round complete?
    if(last_ok && boards < this.max_allowed_boards && total_1 < 25 && total_2 < 25)
      new_board_btn.classList.remove('disabled');
    else
      new_board_btn.classList.add('disabled');
  }

  update_countdown() {
    const self = this,
          countdown_div = document.getElementById('countdown'),
          stop_sign = document.getElementById('stop-sign'),
          new_board_btn = document.getElementById('new_board_btn'),
          end_game_btn = document.getElementById('end_game_btn');

    function update() {
      const {mins, secs, pre_alarm} = self.countdown;

      if(mins || secs) {
        var remaining;

        if(mins > 0)
          remaining = `${mins}'`;
        if(secs > 0) {
          if(mins > 0)
            remaining += ` ${secs}"`;
          else
            remaining = `${secs}"`;
        }
        countdown_div.firstElementChild.innerText = remaining;
        if(pre_alarm) {
          countdown_div.classList.add('pre-alarm');
        }
      } else {
        countdown_div.firstElementChild.classList.add('invisible');
        countdown_div.classList.add('stop');
        stop_sign.classList.remove('invisible');
        end_game_btn.classList.add('blink');
        clearInterval(self.updateInterval);
        self.updateInterval = 0;
      }
    }

    countdown_div.classList.remove('invisible');
    self.updateInterval = setInterval(update, 1000 / 20);
  }

  init(newBoardLabel, confirmEndMessage) {
    const self = this,
          new_board_btn = document.getElementById('new_board_btn');

    $('.checkbox').checkbox();
    new_board_btn.innerText = newBoardLabel;
    new_board_btn.addEventListener('click', (event) => {
      const board = self.played_boards_count;
      var should_add_new_board;

      if(board == 0)
        should_add_new_board = true;
      else if (board >= self.max_allowed_boards)
        should_add_new_board = false;
      else {
        const coins_1_input = document.querySelector(`input[name="coins_${board}_1"]`),
              coins_2_input = document.querySelector(`input[name="coins_${board}_2"]`),
              coins_1 = coins_1_input.value,
              coins_2 = coins_2_input.value,
              queen_1_input = document.getElementById(`cb_queen_${board}_1`).firstElementChild,
              queen_2_input = document.getElementById(`cb_queen_${board}_2`).firstElementChild,
              queen_1 = queen_1_input.checked,
              queen_2 = queen_2_input.checked,
              total_1 = document.getElementById('total_1').innerText,
              total_2 = document.getElementById('total_2').innerText;

        should_add_new_board = ((coins_1 || coins_2)
                                && parseInt(coins_1) < 10
                                && parseInt(coins_2) < 10
                                && (queen_1 || queen_2)
                                && parseInt(total_1) < 25
                                && parseInt(total_2) < 25);
      }

      if(should_add_new_board) {
        var $form = $('form.ui.form'),
            data = $form.serialize(),
            method = $form.attr('method'),
            url = document.URL;
        $.ajax({
          method: method,
          url: url,
          data: data
        }).done(function(result) {
          if(!result.success)
            alert(result.message);
          else if(result.elapsed && !self.started_at) {
            self.started_at = Date.now() - result.elapsed;
            self.update_countdown();
          }
        });
        self.add_board();
      }
    });

    $('thead .checkbox').change(function() {
      new_board_btn.classList.remove('disabled');
    });

    const boards = self.played_boards_count;
    for(var board=1; board <= boards; board++) {
      self.compute_scores_and_totals();
      self.recompute_scores_and_totals_on_change(board);
    }
    $("form").submit(function(event) {
      if(!confirm(confirmEndMessage))
        event.preventDefault();
    });

    if(self.started_at)
      self.update_countdown();
  }
}
