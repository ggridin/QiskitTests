from qiskit_ibm_provider import IBMProvider

from QuantumPlatform import QuantumPlatform


def save_backend_info(platform):
    platform.get_backend_info(coupling_map_filename='coupling_map.png', target_info_filename='target_info.txt')


def print_quantum_job(job):
    if job is None:
        print('quantum job not found!')
        return

    print(f'Job: {job}')
    print(f'Job status: {job.status()}')
    print(f'Job result: {job.result()}')
    print(f'Job result results size: {len(job.result().results)}')
    print(f'Job result results: {job.result().results[0]}')
    if hasattr(job.result(), 'time_taken'):
        print(f'Job time taken(ms): {job.result().time_taken*1000}')
    if hasattr(job.result(), 'metadata'):
        print(f'Job metadata: {job.result().metadata}')
        print(f'Job time taken execute(ms): {job.result().metadata["time_taken_execute"]*1000}')
        print(f'Job time taken parameter binding(ms): {job.result().metadata["time_taken_parameter_binding"]*1000}')
    print('Done!')


def main():
    platform_backend = None
    job_id = 'cqgk89shykgg008ydmq0'
    try:
        platform_backend = QuantumPlatform(IBMProvider(), 'ibm_kyoto')
        save_backend_info(platform_backend)
    except Exception as e:
        print(f'Error during quantum platform initialization: {e}')
        exit(1)

    try:
        job = platform_backend.get_async_job(job_id)
        print_quantum_job(job)
    except Exception as e:
        print(f'Error getting quantum job: {e}')
        exit(1)


main()
