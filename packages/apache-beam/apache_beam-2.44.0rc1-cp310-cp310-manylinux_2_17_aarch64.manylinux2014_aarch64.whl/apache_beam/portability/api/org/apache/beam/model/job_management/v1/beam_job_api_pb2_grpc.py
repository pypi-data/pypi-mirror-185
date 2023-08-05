# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import beam_job_api_pb2 as org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2


class JobServiceStub(object):
    """Job Service for running RunnerAPI pipelines
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Prepare = channel.unary_unary(
                '/org.apache.beam.model.job_management.v1.JobService/Prepare',
                request_serializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.PrepareJobRequest.SerializeToString,
                response_deserializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.PrepareJobResponse.FromString,
                )
        self.Run = channel.unary_unary(
                '/org.apache.beam.model.job_management.v1.JobService/Run',
                request_serializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.RunJobRequest.SerializeToString,
                response_deserializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.RunJobResponse.FromString,
                )
        self.GetJobs = channel.unary_unary(
                '/org.apache.beam.model.job_management.v1.JobService/GetJobs',
                request_serializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobsRequest.SerializeToString,
                response_deserializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobsResponse.FromString,
                )
        self.GetState = channel.unary_unary(
                '/org.apache.beam.model.job_management.v1.JobService/GetState',
                request_serializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobStateRequest.SerializeToString,
                response_deserializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.JobStateEvent.FromString,
                )
        self.GetPipeline = channel.unary_unary(
                '/org.apache.beam.model.job_management.v1.JobService/GetPipeline',
                request_serializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobPipelineRequest.SerializeToString,
                response_deserializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobPipelineResponse.FromString,
                )
        self.Cancel = channel.unary_unary(
                '/org.apache.beam.model.job_management.v1.JobService/Cancel',
                request_serializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.CancelJobRequest.SerializeToString,
                response_deserializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.CancelJobResponse.FromString,
                )
        self.GetStateStream = channel.unary_stream(
                '/org.apache.beam.model.job_management.v1.JobService/GetStateStream',
                request_serializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobStateRequest.SerializeToString,
                response_deserializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.JobStateEvent.FromString,
                )
        self.GetMessageStream = channel.unary_stream(
                '/org.apache.beam.model.job_management.v1.JobService/GetMessageStream',
                request_serializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.JobMessagesRequest.SerializeToString,
                response_deserializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.JobMessagesResponse.FromString,
                )
        self.GetJobMetrics = channel.unary_unary(
                '/org.apache.beam.model.job_management.v1.JobService/GetJobMetrics',
                request_serializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobMetricsRequest.SerializeToString,
                response_deserializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobMetricsResponse.FromString,
                )
        self.DescribePipelineOptions = channel.unary_unary(
                '/org.apache.beam.model.job_management.v1.JobService/DescribePipelineOptions',
                request_serializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.DescribePipelineOptionsRequest.SerializeToString,
                response_deserializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.DescribePipelineOptionsResponse.FromString,
                )


class JobServiceServicer(object):
    """Job Service for running RunnerAPI pipelines
    """

    def Prepare(self, request, context):
        """Prepare a job for execution. The job will not be executed until a call is made to run with the
        returned preparationId.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Run(self, request, context):
        """Submit the job for execution
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetJobs(self, request, context):
        """Get a list of all invoked jobs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetState(self, request, context):
        """Get the current state of the job
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPipeline(self, request, context):
        """Get the job's pipeline
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Cancel(self, request, context):
        """Cancel the job
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStateStream(self, request, context):
        """Subscribe to a stream of state changes of the job, will immediately return the current state of the job as the first response.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMessageStream(self, request, context):
        """Subscribe to a stream of state changes and messages from the job
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetJobMetrics(self, request, context):
        """Fetch metrics for a given job
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribePipelineOptions(self, request, context):
        """Get the supported pipeline options of the runner
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_JobServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Prepare': grpc.unary_unary_rpc_method_handler(
                    servicer.Prepare,
                    request_deserializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.PrepareJobRequest.FromString,
                    response_serializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.PrepareJobResponse.SerializeToString,
            ),
            'Run': grpc.unary_unary_rpc_method_handler(
                    servicer.Run,
                    request_deserializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.RunJobRequest.FromString,
                    response_serializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.RunJobResponse.SerializeToString,
            ),
            'GetJobs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetJobs,
                    request_deserializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobsRequest.FromString,
                    response_serializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobsResponse.SerializeToString,
            ),
            'GetState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetState,
                    request_deserializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobStateRequest.FromString,
                    response_serializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.JobStateEvent.SerializeToString,
            ),
            'GetPipeline': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPipeline,
                    request_deserializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobPipelineRequest.FromString,
                    response_serializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobPipelineResponse.SerializeToString,
            ),
            'Cancel': grpc.unary_unary_rpc_method_handler(
                    servicer.Cancel,
                    request_deserializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.CancelJobRequest.FromString,
                    response_serializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.CancelJobResponse.SerializeToString,
            ),
            'GetStateStream': grpc.unary_stream_rpc_method_handler(
                    servicer.GetStateStream,
                    request_deserializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobStateRequest.FromString,
                    response_serializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.JobStateEvent.SerializeToString,
            ),
            'GetMessageStream': grpc.unary_stream_rpc_method_handler(
                    servicer.GetMessageStream,
                    request_deserializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.JobMessagesRequest.FromString,
                    response_serializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.JobMessagesResponse.SerializeToString,
            ),
            'GetJobMetrics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetJobMetrics,
                    request_deserializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobMetricsRequest.FromString,
                    response_serializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobMetricsResponse.SerializeToString,
            ),
            'DescribePipelineOptions': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribePipelineOptions,
                    request_deserializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.DescribePipelineOptionsRequest.FromString,
                    response_serializer=org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.DescribePipelineOptionsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'org.apache.beam.model.job_management.v1.JobService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class JobService(object):
    """Job Service for running RunnerAPI pipelines
    """

    @staticmethod
    def Prepare(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.beam.model.job_management.v1.JobService/Prepare',
            org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.PrepareJobRequest.SerializeToString,
            org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.PrepareJobResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Run(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.beam.model.job_management.v1.JobService/Run',
            org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.RunJobRequest.SerializeToString,
            org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.RunJobResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetJobs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.beam.model.job_management.v1.JobService/GetJobs',
            org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobsRequest.SerializeToString,
            org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.beam.model.job_management.v1.JobService/GetState',
            org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobStateRequest.SerializeToString,
            org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.JobStateEvent.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPipeline(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.beam.model.job_management.v1.JobService/GetPipeline',
            org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobPipelineRequest.SerializeToString,
            org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobPipelineResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Cancel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.beam.model.job_management.v1.JobService/Cancel',
            org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.CancelJobRequest.SerializeToString,
            org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.CancelJobResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStateStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/org.apache.beam.model.job_management.v1.JobService/GetStateStream',
            org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobStateRequest.SerializeToString,
            org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.JobStateEvent.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMessageStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/org.apache.beam.model.job_management.v1.JobService/GetMessageStream',
            org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.JobMessagesRequest.SerializeToString,
            org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.JobMessagesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetJobMetrics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.beam.model.job_management.v1.JobService/GetJobMetrics',
            org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobMetricsRequest.SerializeToString,
            org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.GetJobMetricsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribePipelineOptions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.beam.model.job_management.v1.JobService/DescribePipelineOptions',
            org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.DescribePipelineOptionsRequest.SerializeToString,
            org_dot_apache_dot_beam_dot_model_dot_job__management_dot_v1_dot_beam__job__api__pb2.DescribePipelineOptionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
