# Agent Check: Kafka Consumer

![Kafka Dashboard][111]

## Overview

This Agent check only collects metrics for message offsets. If you want to collect JMX metrics from the Kafka brokers or Java-based consumers/producers, see the kafka check.

This check fetches the highwater offsets from the Kafka brokers, consumer offsets that are stored in kafka or zookeeper (for old-style consumers), and the calculated consumer lag (which is the difference between the broker offset and the consumer offset).

**Note:** This integration ensures that consumer offsets are checked before broker offsets because worst case is that consumer lag is a little overstated. Doing it the other way around can understate consumer lag to the point of having negative values, which is a dire scenario usually indicating messages are being skipped.

## Setup

### Installation

The Agent's Kafka consumer check is included in the [Datadog Agent][112] package, so you don't need to install anything else on your Kafka nodes.

### Configuration

<!-- xxx tabs xxx -->
<!-- xxx tab "Host" xxx -->

#### Host

To configure this check for an Agent running on a host:

##### Metric collection

1. Edit the `kafka_consumer.d/conf.yaml` file, in the `conf.d/` folder at the root of your [Agent's configuration directory][114]. See the [sample kafka_consumer.d/conf.yaml][113] for all available configuration options.

2. [Restart the Agent][115].

##### Log collection

This check does not collect additional logs. To collect logs from Kafka brokers, see [log collection instructions for Kafka][116].

<!-- xxz tab xxx -->
<!-- xxx tab "Containerized" xxx -->

#### Containerized

For containerized environments, see the [Autodiscovery with JMX][117] guide.

<!-- xxz tab xxx -->
<!-- xxz tabs xxx -->

### Validation

[Run the Agent's status subcommand][118] and look for `kafka_consumer` under the Checks section.

## Data Collected

### Metrics

See [metadata.csv][119] for a list of metrics provided by this check.

### Events

**consumer_lag**:<br>
The Datadog Agent emits an event when the value of the `consumer_lag` metric goes below 0, tagging it with `topic`, `partition` and `consumer_group`.

### Service Checks

The Kafka-consumer check does not include any service checks.

## Troubleshooting

- [Troubleshooting and Deep Dive for Kafka][1110]
- [Agent failed to retrieve RMIServer stub][1111]
- [Producer and Consumer metrics don't appear in my Datadog application][1112]

## Further Reading

- [Monitoring Kafka performance metrics][1113]
- [Collecting Kafka performance metrics][1114]
- [Monitoring Kafka with Datadog][1115]

[111]: https://raw.githubusercontent.com/DataDog/integrations-core/master/kafka_consumer/images/kafka_dashboard.png
[112]: https://app.datadoghq.com/account/settings#agent
[113]: https://github.com/DataDog/integrations-core/blob/master/kafka_consumer/datadog_checks/kafka_consumer/data/conf.yaml.example
[114]: https://docs.datadoghq.com/agent/guide/agent-configuration-files/#agent-configuration-directory
[115]: https://docs.datadoghq.com/agent/guide/agent-commands/#start-stop-and-restart-the-agent
[116]: https://docs.datadoghq.com/integrations/kafka/#log-collection
[117]: https://docs.datadoghq.com/agent/guide/autodiscovery-with-jmx/?tab=containerizedagent
[118]: https://docs.datadoghq.com/agent/guide/agent-commands/#agent-status-and-information
[119]: https://github.com/DataDog/integrations-core/blob/master/kafka_consumer/metadata.csv
[1110]: https://docs.datadoghq.com/integrations/faq/troubleshooting-and-deep-dive-for-kafka/
[1111]: https://docs.datadoghq.com/integrations/faq/agent-failed-to-retrieve-rmierver-stub/
[1112]: https://docs.datadoghq.com/integrations/faq/producer-and-consumer-metrics-don-t-appear-in-my-datadog-application/
[1113]: https://www.datadoghq.com/blog/monitoring-kafka-performance-metrics
[1114]: https://www.datadoghq.com/blog/collecting-kafka-performance-metrics
[1115]: https://www.datadoghq.com/blog/monitor-kafka-with-datadog
