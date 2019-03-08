import ssz

from eth2.beacon.types.proposer_slashings import (
    ProposerSlashing,
)


def test_defaults(sample_proposer_slashing_params):
    slashing = ProposerSlashing(**sample_proposer_slashing_params)
    assert slashing.proposer_index == sample_proposer_slashing_params['proposer_index']
    assert slashing.proposal_1 == sample_proposer_slashing_params['proposal_1']
    assert slashing.proposal_2 == sample_proposer_slashing_params['proposal_2']
    assert ssz.encode(slashing)