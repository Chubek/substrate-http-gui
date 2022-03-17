
from turtle import width
import pyglet
from pyglet import gl
from decode import decode_event_data
from req import get_results


import imgui
# Note that we could explicitly choose to use PygletFixedPipelineRenderer
# or PygletProgrammablePipelineRenderer, but create_renderer handles the
# version checking for us.
from imgui.integrations.pyglet import create_renderer


text_val_dict = {"text_val": "Results will show up here"}

def render_gui():

    window = pyglet.window.Window(width=640, height=480, resizable=True)
    gl.glClearColor(1, 1, 1, 1)
    imgui.create_context()
    impl = create_renderer(window)

    def update(dt):
        imgui.new_frame()

        listof =  ["account_nextIndex","author_insertKey","author_pendingExtrinsics","author_removeExtrinsic","author_rotateKeys","author_submitAndWatchExtrinsic","author_submitExtrinsic","author_unwatchExtrinsic","chain_getBlock","chain_getBlockHash","chain_getFinalisedHead","chain_getFinalizedHead","chain_getHead","chain_getHeader","chain_getRuntimeVersion","chain_subscribeFinalisedHeads","chain_subscribeFinalizedHeads","chain_subscribeNewHead","chain_subscribeNewHeads","chain_subscribeRuntimeVersion","chain_unsubscribeFinalisedHeads","chain_unsubscribeFinalizedHeads","chain_unsubscribeNewHead","chain_unsubscribeNewHeads","chain_unsubscribeRuntimeVersion","contracts_call","state_call","state_callAt","state_getChildKeys","state_getChildStorage","state_getChildStorageHash","state_getChildStorageSize","state_getKeys","state_getMetadata","state_getRuntimeVersion","state_getStorage","state_getStorageAt","state_getStorageHash","state_getStorageHashAt","state_getStorageSize","state_getStorageSizeAt","state_queryStorage","state_subscribeRuntimeVersion","state_subscribeStorage","state_unsubscribeRuntimeVersion","state_unsubscribeStorage","subscribe_newHead","system_accountNextIndex","system_chain","system_health","system_name","system_networkState","system_nodeRoles","system_peers","system_properties","system_version","unsubscribe_newHead"]
        current = listof.index("state_getMetadata")
        imgui.begin("Get and Encode Substrate Results", True)
        imgui.set_window_size(400, 300)
        imgui.text("Select your Action")        
        clicked, current = imgui.combo(
                 "Action", current,listof
        )
        int_val = 1
        
        changed, int_val = imgui.input_int('ID:', int_val)

        

        def get_res():
            results = get_results(str(int_val), listof[current])
            text_val_dict['text_val'] = decode_event_data(results)

        clicked = imgui.button("Run!")

        if clicked:
            get_res()

        text_val = text_val_dict['text_val']
        changed, text_val = imgui.input_text_multiline(
             'Message:',
             text_val,
             112056
            )

        imgui.end()

    def draw(dt):
        update(dt)
        window.clear()
        imgui.render()
        impl.render(imgui.get_draw_data())

    pyglet.clock.schedule_interval(draw, 1/120.)
    pyglet.app.run()
    impl.shutdown()
