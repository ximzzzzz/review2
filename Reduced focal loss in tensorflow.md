```python
class ReducedFocalLoss(object):
    def __init__(self, sample_normalize = None, weight = None, gamma= 2.0, th =0.6):
        self._sample_normalize = sample_normalize
        self._weight = weight
        self.gamma = gamma
        self.th = th
        
    def __call__(self,logits,  labels, lengths):
        
        epsilon = 1e-8
        labels = tf.to_int64(labels)
        labels = tf.convert_to_tensor(labels, tf.int64)
        logits = tf.convert_to_tensor(logits, tf.float32)
        num_cls = logits.shape[-1]
        model_out = tf.add(logits, epsilon)
        onehot_labels = tf.one_hot(labels, num_cls) 
        
        pt = tf.multiply(onehot_labels, model_out)
        ce = tf.multiply(onehot_labels, -tf.math.log(model_out))
        
        pt_sub = tf.math.subtract(1. , pt)
        pt_pow = tf.math.pow(pt_sub, self.gamma)
        div_val = tf.constant(self.th**self.gamma)
        pt_scaled = tf.math.divide(pt_pow, div_val)
        
        fr = tf.where(pt_scaled < 0.5, pt_scaled , tf.ones_like(pt))
        rfl = tf.multiply(fr, ce)
        reduced_rfl = tf.reduce_max(rfl, axis=-1)
        
        batch_size, max_time = shape_utils.combined_static_and_dynamic_shape(labels)
        mask = tf.less(
            tf.tile([tf.range(max_time)], [batch_size, 1]),
            tf.expand_dims(lengths, 1),
            name='mask'
            )
        masked_losses = tf.multiply(
            reduced_rfl,
            tf.cast(mask, tf.float32),
            name='masked_losses'
            ) # => [batch_size, max_time]
        row_losses = tf.reduce_sum(masked_losses, 1, name='row_losses')
        loss = tf.reduce_sum(row_losses)
        if self._sample_normalize:
            loss = tf.truediv(
              loss,
              tf.cast(tf.maximum(batch_size, 1), tf.float32))
        if self._weight:
            loss = loss * self._weight
    
        return loss
```

