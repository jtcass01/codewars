#include <string>

using namespace std;

class Player {
private:
  unsigned int base;
  bool score;
public:
  Player();
  void advance(const string &);
  inline bool getScore(void){return score;}
  inline unsigned int getBase(void){return base;}
  friend ostream& operator<<(ostream& os, Player p){
    os << "Base: " << p.getBase() << "\t" << "Score: " << p.getScore();
    return os;
  }
};

class ScoreCard {
private:
  unsigned int awayScore;
  unsigned int homeScore;
  unsigned int outs;
  bool awayUp;
  vector<Player> playersOnBase;
public:
  ScoreCard();
  void addEntry(const string &);
  string getScore(void);
  unsigned int tallyScores(vector<Player>);
  void removeScorers(void);
  void printPlayersOnBase(){
    for(unsigned int player_i = 0; player_i < playersOnBase.size(); player_i++){
      cout << playersOnBase[player_i] << endl;
    }
  }
  inline unsigned int getAwayScore(void){return awayScore;}
  inline unsigned int getHomeScore(void){return homeScore;}
  inline unsigned int getOuts(void){return outs;}
};

ScoreCard::ScoreCard(void){
  awayScore = 0;
  homeScore = 0;
  outs = 0;
  awayUp = true;
}

string ScoreCard::getScore(void){
  return "Home: " + to_string(homeScore) + " Away: " + to_string(awayScore);
}

void ScoreCard::addEntry(const string &entry){
  ScoreCard score_card;
  Player batter;

  if(!entry.compare("out")){
    outs += 1;
  } else {
    batter.advance(entry);
    for(unsigned int player_i = 0; player_i < playersOnBase.size(); player_i++){
      playersOnBase[player_i].advance(entry);
    }
    playersOnBase.insert(playersOnBase.begin(), batter);
  }

  if(awayUp){
    awayScore += tallyScores(playersOnBase);
    removeScorers();
    
    if(outs >= 3){
      awayUp = false;
      outs = 0;
      playersOnBase.clear();
    }
  } else {
    homeScore += tallyScores(playersOnBase);
    removeScorers();
    
    if(outs >= 3){
      awayUp = true;
      outs = 0;
      playersOnBase.clear();
    }
  }
}

unsigned int ScoreCard::tallyScores(vector<Player> players){
  unsigned int result = 0;

  for(unsigned int player_i = 0; player_i < players.size(); player_i++){
    if(players[player_i].getScore() == true){
      result += 1;
    }
  }
  
  return result;
}

void ScoreCard::removeScorers(void){
  vector<Player> playersNotScored;

  for(unsigned int player_i = 0; player_i < playersOnBase.size(); player_i++){
    if(playersOnBase[player_i].getScore() != true){
      playersNotScored.insert(playersNotScored.begin(), playersOnBase[player_i]);
    }
  }

  playersOnBase = playersNotScored;
}

Player::Player(void){
  base = 0;
  score = false;
}

void Player::advance(const string &str){
  if(str == "single"){
    base += 1;
  } else if (str == "double") {
    base += 2;
  } else if (str == "triple") {
    base += 3;
  } else if (str == "homerun") {
    base += 4;
  }
  
  if(base >= 4){
    score = true;
  }
}
