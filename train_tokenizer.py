from tokenizers import Tokenizer, models, pre_tokenizers, decoders, processors, trainers
from os import listdir
from config import tokenizer_train_path as train_path


# Initialize a tokenizer
tokenizer = Tokenizer(models.BPE())

tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=True)
tokenizer.decoder = decoders.ByteLevel()
tokenizer.post_processor = processors.ByteLevel(trim_offsets=True)


tokenizer_trainer = trainers.BpeTrainer(
    vocab_size=32786,
    min_frequency=2,
    initial_alphabet=pre_tokenizers.ByteLevel.alphabet(),
    show_progress=True,
    special_tokens=["<s>", "<pad>", "</s>", "<unk>", "<mask>"],
)


tokenizer.train([train_path + x for x in listdir(train_path)], tokenizer_trainer)
tokenizer.save(train_path + "tokenizer.json", pretty=True)
