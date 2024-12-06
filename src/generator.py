from hypothesis.strategies import SearchStrategy, composite, sampled_from, text, lists, integers
from typing import Callable
import string
import us
from .datatype import Vote


@composite
def vote_gen(draw: Callable[[SearchStrategy], str]) -> Vote:
    election_ids = ["PRESIDENTIAL_2024_PRIMARIES", "PRESIDENTIAL_2024_GENERAL"]
    candidate_names = ["Alice", "Bob", "Charlie"]
    all_states = [state.name for state in us.states.STATES]
    
    election_id = draw(sampled_from(election_ids))
    candidate_name = draw(sampled_from(candidate_names))
    voter_id = draw(text(min_size=1, max_size=10, alphabet=string.ascii_letters)) 
    age = draw(integers(min_value=18, max_value=90))
    gender = draw(sampled_from(["male", "female", "other"]))
    region = draw(sampled_from(all_states))
    race = draw(sampled_from(["Asian", "White", "Black", "Hispanic", "Other"]))
    education = draw(sampled_from(["HighSchool", "Bachelor", "Master", "PhD"]))
    
    attributes = {
        "age": age,
        "gender": gender,
        "region": region,
        "race": race,
        "education": education
    }
    
    return Vote(election_id=election_id, candidate_name=candidate_name, voter_id=voter_id, attributes=attributes)

vote_list_gen = lists(vote_gen(), min_size=50, max_size=100)