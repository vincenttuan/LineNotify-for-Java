package com.linenotify;

class LineParameter {
    private String message;
    private int stickerPackageId;
    private int stickerId ;

    public LineParameter(String message) {
        this.message = message;
    }
    
    public LineParameter(String message, int stickerPackageId, int stickerId) {
        this.message = message;
        this.stickerPackageId = stickerPackageId;
        this.stickerId = stickerId;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public int getStickerPackageId() {
        return stickerPackageId;
    }

    public void setStickerPackageId(int stickerPackageId) {
        this.stickerPackageId = stickerPackageId;
    }

    public int getStickerId() {
        return stickerId;
    }

    public void setStickerId(int stickerId) {
        this.stickerId = stickerId;
    }
    
    
}
